class TrieNode{
    public:
    unordered_map<char, TrieNode*> children;
    string word = "";
    TrieNode(){}
};
class Solution {
public:
    // instance variable to be able to access board outside of findWords
    vector<vector<char>> theboard;
    vector <string> ans;

    // backtracking function
    void backtracking(int row, int col, TrieNode* parent){
        char letter = theboard[row][col];
        
        // Check if the current letter is in the children map
        if (!parent->children.count(letter)) {
            return; // No corresponding node in the trie, exit the function
        }

        TrieNode* currNode = parent->children[letter];

        if (currNode->word.length() > 0){
            ans.push_back(currNode->word);
            currNode->word = ""; // avoid duplicating answers
        }

        // mark the current letter as visited before the exploration
        theboard[row][col] = '#';

        // expore neighbor cells in 4 possible directions (clockwise: up, right, down, left)
        int rowoffset[4] = {-1, 0, 1, 0};
        int coloffset[4] = {0, 1, 0, -1};
        
        for(int i = 0; i < 4; i++){
            int newrow = row + rowoffset[i];
            int newcol = col + coloffset[i];

            // check if the neighboring node is out of bounds
            if (newrow < 0 || newrow >= theboard.size() || newcol < 0 || newcol >= theboard[0].size()){
                continue; // disregard
            }
            
            if (currNode->children.count(theboard[newrow][newcol])){
                backtracking(newrow, newcol, currNode);
            }
        }

        // end of exploration restore original letter in the board
        theboard[row][col] = letter;

        // optimization: time complexity of the algorithm depends on size of Trie
        // once we traverse leaf node would no longer need to traverse it again
        if (currNode->children.size() == 0){
            parent->children.erase(letter);
        }
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // step 1: build the Trie out of the words in the words list
        TrieNode root; // creating the root node
        for(string word: words){
            TrieNode* node = &root;
            for(char letter: word){
                if (node->children.count(letter)){
                    node = node->children[letter];
                } else{
                    TrieNode* newnode = new TrieNode(); // allocating memory using new
                    node->children[letter] = newnode;
                    node = newnode;
                }
            }
            node->word = word;
        }

        // step 2: backtracking starting from each cell in the board
        theboard = board;
        int m = board.size();
        int n = board[0].size();

        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                backtracking(row, col, &root);
            }
        }

        return ans;
    }
};
