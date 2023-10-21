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
// inorder traversal
// N = number of nodes time: O(N) 
// space: O(N) worst case memory from recursion stack when binary search tree is completely skewed
class Solution {
public:
    long long int prev = LLONG_MIN;
    bool inorderTraversal(TreeNode* current){
        // basecase: reach null node
        if (current == NULL)
            return true;
        
        // iterate through left node
        if (!inorderTraversal(current->left))
            return false;
        
        // check current node
        if (current->val <= prev)
            return false;

        prev = current->val;
        
        return inorderTraversal(current->right);
    }
    bool isValidBST(TreeNode* root) {
        // validate by checking if it is strictly larger through inorder traversal
        return inorderTraversal(root);
    }
};
