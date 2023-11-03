// time: O(NlogN) space: O(1)
class Solution {
public:
    // customized sorting function that compares two intervals
    static bool cmp(vector<int> a, vector<int> b){
        if (a[0] == b[0]){
            return a[1] < b[1];
        } else{
            return a[0] < b[0];
        }
    }

    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if (intervals.size() == 0)
            return true;
        
        sort(intervals.begin(), intervals.end(), cmp);

        int curend = intervals[0][1];
        for (int i=1; i< intervals.size(); i++){
            vector<int> curinterval = intervals[i];
            int start = curinterval[0];
            int end = curinterval[1];

            if (start < curend)
                return false;

            curend = end;
        }
        /*
        ending 
        1) nextstart <= ending -> false
        2) nextstart > ending -> continue
        */
        return true;
    }
};
