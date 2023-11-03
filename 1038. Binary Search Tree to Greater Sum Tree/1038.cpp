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
// modified inorder traversal: right -> root -> left
// time: O(N), space:O(N)
class Solution {
public:
    int cursum = 0;
    void gstiter(TreeNode* curNode){
        // base case: reach righmost node
        if (curNode->left == NULL && curNode->right == NULL){
            curNode->val += cursum;
            cursum = curNode->val;
            return;
        }

        if (curNode->right != NULL){
            gstiter(curNode->right);
        }
        curNode->val += cursum;
        cursum = curNode->val;

        if (curNode->left != NULL){
            gstiter(curNode->left);
        }

    }

    TreeNode* bstToGst(TreeNode* root) {
        gstiter(root);
        return root;
    }
};
