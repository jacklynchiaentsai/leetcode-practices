class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // sort + priority queue
        // time: O(nlogn) space: O(n)
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b){
            if (a[0] == b[0])
                return a[1] < b[1];
            else
                return a[0] < b[0];
        });

        priority_queue<int, vector<int>, greater<int>> end_times;

        for(int i = 0; i<n; i++){
            int start = intervals[i][0];
            int end = intervals[i][1];
            // need a new room
            if (end_times.empty() || start < end_times.top()){
                end_times.push(end);
            } else{
                end_times.pop();
                end_times.push(end);
            }
        }

        return end_times.size();
    }
};
