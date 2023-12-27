/*
recursive helper functions
-> for averages separate sum and numnodes for more intuitiveness
visiting each node only once
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
    double maximumAverageSubtree(TreeNode* root) {
        return getmaxavg(root);
    }

    double getmaxavg(TreeNode* curNode){
        if (curNode == nullptr){
            return 0.0;
        }
        return max(calcavg(curNode), max(getmaxavg(curNode->left), getmaxavg(curNode->right)));
    }

    double calcavg(TreeNode* curNode){
        if (numnodes(curNode) == 0){
            return 0.0;
        }
        return 1.0 * sumofsubtree(curNode) / numnodes(curNode);
    }

    int sumofsubtree(TreeNode* curNode){
        if (curNode == nullptr){
            return 0;
        }

        if (curNode->left == nullptr && curNode->right == nullptr){
            return curNode->val;
        }

        return sumofsubtree(curNode->left) + sumofsubtree(curNode->right) + curNode->val;
    }

    int numnodes(TreeNode* curNode){
        if (curNode == nullptr){
            return 0;
        }

        if (curNode->left == nullptr && curNode->right == nullptr){
            return 1;
        }

        return numnodes(curNode->left) + numnodes(curNode->right) + 1;
    }
};
