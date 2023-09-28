class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // sort + two pointers
        // time: O(nlogn) space: O(n)
        int n = intervals.size();
        vector<int> start_times;
        vector<int> end_times;

        for(vector<int> arr: intervals){
            start_times.push_back(arr[0]);
            end_times.push_back(arr[1]);
        }

        sort(start_times.begin(), start_times.end());
        sort(end_times.begin(), end_times.end());

        int startIndex = 0, endIndex = 0, rooms = 0;
        while(startIndex < start_times.size()){
            int start = start_times[startIndex];
            int end = end_times[endIndex];
            if (start < end)
                rooms++;
            else{
                endIndex++;
            }
            startIndex++;
        }

        return rooms;
    }
};
