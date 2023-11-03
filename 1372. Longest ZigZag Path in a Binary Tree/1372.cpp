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

// top down recursive approach
// N = number of nodes-> time: O(N), space: O(N) from recursion stack
class Solution {
    public:
        int longestLength = 0;

        void zigzagLength(TreeNode* currentNode, bool goLeft, int steps){
            
            longestLength = max(longestLength, steps);
            
            // base case: reach leaf node
            if (currentNode->right == NULL && currentNode->left == NULL){
                return;
            }

            if (goLeft){
                if (currentNode->right != NULL){
                    zigzagLength(currentNode->right, false, steps + 1);
                }
                
                if (currentNode-> left != NULL){
                    zigzagLength(currentNode->left, true, 1);
                }
            } else{
                if (currentNode->left != NULL){
                    zigzagLength(currentNode->left, true, steps + 1);
                }
                if (currentNode->right != NULL){
                    zigzagLength(currentNode->right, false, 1);
                } 
            }
        }

        int longestZigZag(TreeNode* root) {
            zigzagLength(root, true, 0);
            zigzagLength(root, false, 0);
            return longestLength;
        }
};
