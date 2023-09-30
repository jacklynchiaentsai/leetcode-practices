// time: O(NlogN) due to sorting
// space: O(N)
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // hashmap to store frequency
        // sorting with pairs
        unordered_map<string, int> word_freq;

        for(string word: words){
            word_freq[word]++;
        }

        vector<pair<int, string>> freq_order;
        for(auto it: word_freq){
            freq_order.push_back({-it.second, it.first});
        }

        sort(freq_order.begin(), freq_order.end());

        vector<string> ans;

        for(int i=0; i<k; i++){
            ans.push_back(freq_order[i].second);
        }

        return ans;
    }
};
