// try finding longest mountain everytime I find a potential starting point
// take care of edge cases
// time: O(N)
// space: O(1)
class Solution {
public:
    int longestMountain(vector<int>& arr) {
        // start is starting index of mountain array
        int maxlen = 0, start = -1;
        bool curincreasing = true;


        for(int i =0; i< arr.size() - 1; i++){
            // check if it is starting point of mountain
            if (arr[i] < arr[i+1]){
                start = i;
                bool hasincreasing = false, hasdecreasing = false;
                // find mountain length
                while (arr[i] < arr[i+1]){ // increasing
                    i++;
                    hasincreasing = true;
                    // end of array is increasing return answer immediately
                    if ((i+1) >= arr.size()){
                        return maxlen;
                    }
                }
                while (arr[i] > arr[i+1]){ // decreasing
                    i++;
                    hasdecreasing = true;
                    if ((i+1) >= arr.size()){
                        break;
                    }
                }

                if (hasincreasing && hasdecreasing){
                    maxlen = max(maxlen, i - start + 1);
                    // ending point can potentially be starting point for next
                    i--;
                }

            }
            
        }

        return maxlen;
    }
};
