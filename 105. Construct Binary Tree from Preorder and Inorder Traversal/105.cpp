/*
recursion
- preorder gives us the root node of every subtree
- inorder gives us the range of the left and right subtrees
N; nodes in binary tree
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int preorder_indx = 0;
        return buildsubtree(preorder_indx, preorder, inorder, 0, inorder.size() - 1);
    }

    TreeNode* buildsubtree(int& preorder_index, vector<int>& preorder, vector<int>& inorder, int inorder_start, int inorder_end){
        // base case
        if (inorder_start > inorder_end)
            return nullptr;
        
        int root_val = preorder[preorder_index];
        TreeNode* rootNode = new TreeNode(root_val);
        preorder_index += 1; // update index pointer of preorder array
        int root_at_inorder;
        
        // find index of root node at inorder array
        for(int i = inorder_start; i<= inorder_end; i++){
            if (inorder[i] == root_val){
                root_at_inorder = i;
                break;
            }
        }

        // left subtree is within the index range: [inorder_start, root_at_inorder - 1]
        rootNode->left = buildsubtree(preorder_index, preorder, inorder, inorder_start, root_at_inorder - 1);
        rootNode->right = buildsubtree(preorder_index, preorder, inorder, root_at_inorder + 1, inorder_end);
        
        return rootNode;
    }
};
