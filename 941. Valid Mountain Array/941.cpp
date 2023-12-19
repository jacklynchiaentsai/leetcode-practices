// time: O(N)
// space: O(1)
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3)
            return false;   

        bool increasing = true;
        int maxele = -1;
        for(int ele: arr){
            maxele = max(maxele, ele);
        }
        
        // peak can't be first or last
        // make sure that there is both increasing and decreasing component in array
        if (maxele == arr[arr.size()-1] || maxele == arr[0])
            return false;

        bool increase = true;
        for(int i =0; i< arr.size()-1; i++){
            if (arr[i] == maxele){
                increase = false;
            }
            // compare with next element
            if (increase && arr[i] >= arr[i+1]){
                return false;
            } else if (!increase && arr[i] <= arr[i+1]){
                return false;
            }
        }
        return true;
    }
};
