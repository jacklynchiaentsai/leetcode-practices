/*
breadth first search traversal
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
    
    vector<vector<int>> levelOrder(TreeNode* root) {

        vector<vector<int>> ans;
        if (root == nullptr){
            return ans;
        }

        queue<pair<TreeNode*, int>> tree_queue;
        tree_queue.push({root, 0});

        vector<int> level_vec;
        int curlevel = -1;

        while(!tree_queue.empty()){
            TreeNode* curNode = tree_queue.front().first;
            int level = tree_queue.front().second;
            tree_queue.pop();

            // reached new level
            if (level > curlevel && level != 0){
                ans.push_back(level_vec);
                level_vec.clear();
                curlevel = level;
            }

            int value = curNode->val;
            level_vec.push_back(value);
            
            if (curNode->left != nullptr)
                tree_queue.push({curNode->left, level + 1});
            if (curNode->right != nullptr)
                tree_queue.push({curNode->right, level + 1});
        }

        ans.push_back(level_vec);

        return ans;

    }
};
