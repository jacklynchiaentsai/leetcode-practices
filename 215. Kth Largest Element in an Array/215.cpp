// using priority queue
// time: O(nlogk) due to insertion
// space: O(k)
// sorting takes time: O(nlogn), space: O(logn)
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int num: nums){
            if (pq.size() <k){
                pq.push(num);
            } else{
                if (pq.top() < num){
                    pq.pop();
                    pq.push(num);
                }
            }
        }

        return pq.top();
    }
};
