/*
union find, multipath recursion (depth first search)
N: number of words in text
M: pairs of synonym
K: number of unique words in synonyms
worst case number of combinations can be K^N
time: O(K*K + N*K + K^N log(K^N))
space: O(K^N)
*/
class Solution {
public:

    vector<string> combinations;

    vector<string> split_sent(string sentence){
        stringstream ss(sentence);
        string temp;
        vector<string> parsed;
        while(ss >> temp){
            parsed.push_back(temp);
        }
        return parsed;
    }

    string findHead(string word, unordered_map<string, string>& head_map){  
        if (head_map.find(word) == head_map.end()){
            head_map[word] = word;
            return word;
        } else if (head_map[word] == word){
            return word;
        } else{
            return findHead(head_map[word], head_map);
        }
    }

    void genWord(int startindex, vector<string> text_vec, unordered_map<string, set<string>>& syn_groups, unordered_map<string, string>& head_map, string curSent){
        
        if (startindex >= text_vec.size()){
            combinations.push_back(curSent.substr(0, curSent.length()-1));
            return;
        }

        string curWord = text_vec[startindex];
        string headWord = findHead(curWord, head_map);

        // word does not have synonyms
        if (syn_groups.find(headWord)== syn_groups.end()){
            genWord(startindex+1, text_vec, syn_groups, head_map, curSent + curWord + " ");
        } else{
            for (string synonym: syn_groups[headWord]){
                genWord(startindex+1, text_vec, syn_groups, head_map, curSent + synonym + " ");
            }
        }
    }

    vector<string> generateSentences(vector<vector<string>>& synonyms, string text) {
        
        unordered_map<string, string> head_map;
        unordered_map<string, set<string>> syn_groups;

        for(auto wordpair: synonyms){
            string word1 = wordpair[0];
            string word2 = wordpair[1];
            string head_word1 = findHead(word1, head_map);
            string head_word2 = findHead(word2, head_map);

            if (head_word1.compare(head_word2) < 0){
                head_map[head_word2] = head_word1;
            } else{
                head_map[head_word1] = head_word2;
            }
        }

        // building up syn_groups
        for(auto it: head_map){
            string word = it.first;
            string head_word = findHead(word, head_map);
            syn_groups[head_word].insert(word);
        }

        vector<string> text_vec = split_sent(text);
        genWord(0, text_vec, syn_groups, head_map, "");

        sort(combinations.begin(), combinations.end());
        return combinations;
    }
};
/*
- a word can be synonyms with multiple words
- vector<string> text = "I am happy today"
["I am happy today", "I am joyful today"]

head = {"word": "head_word"}
syn_groups = {"head_word": ["synonym1", "synonym2"]}
*/
