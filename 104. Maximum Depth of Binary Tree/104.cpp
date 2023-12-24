/*
recursive helper function, binary tree traversal
n: number of nodes
time: O(n) -> traversing through every node
space: (recursive stack)
- O(log(n)) if tree is completely balanced
- O(n) if tree is completely unbalanced
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
    int maxDepth(TreeNode* root) {
        return findDepth(root, 0);
    }

    int findDepth(TreeNode* curNode, int depth){
        if (curNode == nullptr){
            return depth;
        }
        
        int leftdepth = findDepth(curNode->left, depth + 1);

        int rightdepth = findDepth(curNode->right, depth + 1);

        return max(leftdepth, rightdepth);
    }
};
