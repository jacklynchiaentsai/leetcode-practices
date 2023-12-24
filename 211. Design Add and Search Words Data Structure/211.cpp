/*
Trie Data Strucuture + recursive helper function
m = word length
time complexity:
- addWord: O(m)
- search: 
    - O(m) -> searching defined words
    - O(N * 26^m ) -> worst case situation of searching undefined word with all .
space complexity:
- addWord: O(m)
- search: 
    - O(1) -> searching well defined words
    - O(m) -> recursion stack
*/
class TrieNode{
public:
    bool endofword;
    unordered_map<char, TrieNode*> children;

    TrieNode(bool isend){
        this->endofword = isend;
    }
};

class WordDictionary {
public:
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode(false);
    }
    
    void addWord(string word) {
        TrieNode* currNode = root;
        for(char ch: word){
            if (currNode->children.find(ch) == currNode->children.end()){
                // not found
                currNode->children[ch] = new TrieNode(false);
            }

            currNode = currNode->children[ch];
        }

        currNode->endofword = true;
    }
    
    bool search(string word) {
        return searchintree(word, this->root);
    }

    bool searchintree(string word, TrieNode* currNode){
        // base case is when word length = 1 but repeats the same operation as below
        int i = 0;
        while( i < word.length()){
            char curchar = word[i];
            if (curchar != '.'){
                if (currNode->children.find(curchar) == currNode->children.end()){
                    return false;
                }
                currNode = currNode->children[curchar];
            } else{
                for (auto it: currNode->children){
                    char key = it.first;
                    TrieNode* node = it.second;
                    if (searchintree(word.substr(i+1), node)){
                        return true;
                    }
                }
                return false;
            }
            i++;
        }

        // final check if it is end of word
        return currNode->endofword;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
