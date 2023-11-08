// using segment tree
class NumArray {
public:
    // attributes of class
    vector<int> segtree;
    int n;

    // building segment tree with array: bottom up approach
    // time: O(n) total of 2n nodes, space: O(n)
    NumArray(vector<int>& nums) {
        n = nums.size();
        // binary tree with n leaves: total leaves = n+n/2+n/4+n/8+…+1≈2n
        segtree= vector<int>(n*2);
        buildTree(nums);
    }
    
    // bottom-up rebuild the segment tree that contains the sum of the modified element
    // time: O(log(n)) # of levels in segment tree space: O(1) updating existing tree
    void update(int index, int val) {
        // update the corresponding index in segment tree
        int updateindex = index + n;
        segtree[updateindex] = val;

        // update bottom up
        while(updateindex > 0){
            int left, right;

            // if the index I am updating is the left node
            if (updateindex % 2  == 0){
                left = updateindex;
                right = left + 1;
            } else{
                right = updateindex;
                left = right - 1;
            }

            // update the parent node that holds the sum
            segtree[updateindex / 2] = segtree[left] + segtree[right];
            updateindex /= 2;
        }
    }
    
    // bottom up approach
    // time: O(log(n)) in each iteration we move one level up space: O(1)
    int sumRange(int left, int right) {
        int sum = 0;
        // get corresponding index in segment tree 
        int cur_l = left + n;
        int cur_r = right + n;

        while (cur_l <= cur_r){
            // if cur_l is the right node of its parent
            if (cur_l % 2 == 1){
                // we don't need the parent's sum we just need the element itself
                sum += segtree[cur_l];
                // after including the element in cur_l in our sum we move our left bound forward
                cur_l++;
            }

            // if cur_r is the left node of its tree
            if (cur_r % 2 == 0){
                // we don't need the parent's sum we just need the element itself
                sum += segtree[cur_r];
                cur_r--;
            }

            cur_l /= 2;
            cur_r /= 2;
        }

        return sum;
    }

private:
    void buildTree(vector<int> nums){
        // begin from leaves, initialize with input array elements
        int nums_index = 0;
        for(int i = n; i < n*2; i++){
            segtree[i] = nums[nums_index];
            nums_index++;
        }
        // update the remaining layers bottom up
        // note: not using the index 0
        for(int i = n-1; i >= 1; i--){
            // the sum of left and right nodes
            segtree[i] = segtree[i*2] + segtree[i*2 + 1];
        }
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
