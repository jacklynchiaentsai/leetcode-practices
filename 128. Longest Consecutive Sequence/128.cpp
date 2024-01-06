/*
- hashmaps have O(1) find time complexity
- O(n) can mean multiple independent iterations

- time: O(n)
- space: O(n)
*/
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // true: visited, false: not yet
        unordered_map<int, bool> ele_map;
        int maxlen = 0;
        
        for(int num: nums){
            ele_map[num] = false;
        }

        for(int num: nums){
            if (ele_map[num]){
                continue;
            }

            int templen = 1;
            int smallernum = num - 1, largernum = num + 1;

            while(ele_map.find(smallernum) != ele_map.end()){
                ele_map[smallernum--] = true;
                templen++;
            }

            while(ele_map.find(largernum) != ele_map.end()){
                ele_map[largernum++] = true;
                templen++;
            }

            maxlen = max(maxlen, templen);
        }

        return maxlen;
    }
};
