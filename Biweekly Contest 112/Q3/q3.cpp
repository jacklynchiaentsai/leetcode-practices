class Solution {
public:
    long long maxSum(vector<int>& nums, int m, int k) {
        unordered_map<int, int> freq_map;
        long long int maxsum = 0;
        int distinctCount = 0;
        
        for(int i = 0; i< nums.size(); i++){
            if (freq_map.count(nums[i]))
                freq_map[nums[i]]++;
            else
                freq_map[nums[i]] = 1;
            
            if (freq_map[nums[i]] == 1) {
                distinctCount++;
            } 
            
            // Maintain the sliding window size k
            if (i >= k) {
                int leftElement = nums[i - k];
                freq_map[leftElement]--;

                // If the left element's frequency becomes zero, decrement distinctCount
                if (freq_map[leftElement] == 0) {
                    distinctCount--;
                }
            }
            
              
            if (distinctCount >= m) {
                long long int tempSum = 0;
                int tempcount = 0;
                for (int j = i; j >= 0 && tempcount < k; j--) {
                    tempSum += nums[j];
                    tempcount += 1;
                }

                maxsum = max(maxsum, tempSum);
            }
            
            
        }
        
        return maxsum;
    }
};
