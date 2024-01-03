/*
preorder traversal, dummy root node
time: O(N)
space: O(N)
*/
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
class Solution {
public:

    TreeNode* listNode;

    void flatten(TreeNode* root) {
        if (root == nullptr){
            return;
        }

        listNode = new TreeNode();
        TreeNode* copylistNode = listNode;
        buildList(root);
        root->left = nullptr;
        root->right = copylistNode->right->right;
    }

    void buildList(TreeNode* curNode){
        if (curNode == nullptr){
            return;
        }

        TreeNode* addingNode = new TreeNode(curNode->val);
        listNode->right = addingNode;
        listNode = listNode->right;

        buildList(curNode->left);
        buildList(curNode->right);
    }
};
