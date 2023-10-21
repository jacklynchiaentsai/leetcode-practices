/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
// top down in order traversal
// N = number of nodes time: O(N) 
// space: O(N) worst case memory from recursion stack when binary search tree is completely skewed
class Solution {
public:
    bool validateTree(TreeNode* current, long long int low, long long int high){
        // basecase: reach null node
        if (current == NULL)
            return true;
        
        int value = current->val;
        
        // not within range
        if (value <= low || value >= high)
            return false;
        
        // recursive inorder traversal
        return validateTree(current->left, low, value) && validateTree(current->right, value, high);
        
    }
    bool isValidBST(TreeNode* root) {
        // validate by recursively updating range
        return validateTree(root, LLONG_MIN, LLONG_MAX);
    }
};
