// binary search of two arrays at once
// worst case need to cut both arrays before finding target element
// time: O(log(m) + log(n)) = O(log(mn)) -> depends on when one of the arrays is cut into an empty array
// space: O(1)
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        int tot_size = len1 + len2;

        // determine the target indices and the range od each array (recursive
        // binary search)
        if (tot_size % 2 == 1) {
            return solvekth(nums1, nums2, tot_size / 2, 0, len1 - 1, 0,
                            len2 - 1);
        } else {
            return 1.0 *
                   (solvekth(nums1, nums2, tot_size / 2 - 1, 0, len1 - 1, 0,
                             len2 - 1) +
                    solvekth(nums1, nums2, tot_size / 2, 0, len1 - 1, 0,
                             len2 - 1)) /
                   2;
        }
    }

    int solvekth(vector<int>& A, vector<int>& B, int k, int astart, int aend, int bstart, int bend) {
        // if the segment of one array is empty it means we passed all its elemenet return corresponding element in the other array
        if (astart > aend){
            return B[k - astart];
        } 

        if (bstart > bend){
            return A[k-bstart];
        }

        int amid = astart + (aend - astart) / 2, bmid = bstart + (bend - bstart) / 2;
        int aval = A[amid], bval = B[bmid];
        
        // if k is in the right half of A+B remove the smaller left half
        if (k > amid + bmid){
            // determine if it is removing A_left or B_left
            if (aval > bval){ // remove B_left
                return solvekth(A, B, k, astart, aend, bmid + 1, bend);
            } else{
                return solvekth(A, B, k, amid + 1, aend, bstart, bend);
            }
        } else{
            if (aval > bval){ // remove A_right
                return solvekth(A, B, k, astart, amid - 1, bstart, bend);
            } else{
                return solvekth(A, B, k, astart, aend, bstart, bmid - 1);
            }
        }

    }
};
