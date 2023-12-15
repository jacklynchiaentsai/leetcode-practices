// intelligently build subsequence + binary search
// time: O(nlog(n))
// space: O(n)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // build increasing subsequence (not always valid subsequence but the length will always equal the length of the longest increasing subsequence)
        vector<int> subseq;
        for (int num: nums){
            // expand subsequence
            if (subseq.size() == 0 || num > subseq[subseq.size()- 1]){
                subseq.push_back(num);
            } else{
                // replace the first num that is greater than or equal to num
                // length is maintained but once I find a longer substring I can extend it 
                // can use binary search since it's sorted
                bool eqfound = false;
                int start = 0, end = subseq.size() - 1;
                while(start <= end){
                    int mid = start + (end-start) / 2;
                    if (subseq[mid] == num){
                        eqfound = true;
                        break;
                    } else if (num < subseq[mid]){
                        end = mid - 1;
                    } else{
                        start = mid + 1;
                    }
                }
                // if can't find element want to 
                if (!eqfound){
                    subseq[start] = num;
                }

            }
        }
        return subseq.size();
    }
};
