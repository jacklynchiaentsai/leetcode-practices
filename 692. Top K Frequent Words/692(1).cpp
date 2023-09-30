// time: O(Nlogk) due to insertion with prioirity queue within loop
// space: O(N)
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // hashmap to store frequency
        // using minheap (priority queue)
        // if I'm selecting k best candidates every time a new item comes in I only care if it's better than the worst on my list so far

        unordered_map<string, int> word_freq;

        for(string word: words){
            word_freq[word]++;
        }

        priority_queue<pair<int, string>> pq;
        for(auto it: word_freq){
            pq.push({-it.second, it.first});

            if (pq.size() > k){
                pq.pop();   // remove the worst
            }
        }

        vector<pair<int, string>> candidates;
        vector<string> ans;
        while(!pq.empty()){
            candidates.push_back(pq.top());
            pq.pop();
        }

        sort(candidates.begin(), candidates.end()); // only with k candidates: k*log(k)
        for(int i=0; i<k; i++){
            ans.push_back(candidates[i].second);
        }

        return ans;
    }
};
