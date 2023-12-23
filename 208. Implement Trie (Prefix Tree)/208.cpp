/*
m: length of word
time complexity:
- insert: O(m)
- search: O(m)
- startsWith: O(m)

space complexity:
- insert: O(m)
- search: O(1)
- startsWith: O(1)
*/

class TrieNode{
public:
    bool endofword;
    unordered_map<char, TrieNode*> children;
    TrieNode(bool isend){
        this->endofword = isend;
    }
};

class Trie {
public:
    TrieNode* root;
    
    Trie() {
        // initiate root node
        root = new TrieNode(false);
    }
    
    void insert(string word) {
        TrieNode *curNode = this->root;
        for(char ch: word){
            if (curNode->children.find(ch) == curNode->children.end()){
                curNode->children[ch] = new TrieNode(false);
            } 

            curNode = curNode->children[ch];
        }
        // set the last to be true
        curNode->endofword = true;
    }
    
    bool search(string word) {
        TrieNode *curNode = this->root;
        for(char ch: word){
            if (curNode->children.find(ch) == curNode->children.end()){
                return false;
            } 
            curNode = curNode->children[ch];
        }

        if (curNode->endofword == true)
            return true;
        else
            return false;
    }
    
    bool startsWith(string prefix) {
        TrieNode *curNode = this->root;
        for(char ch: prefix){
            if (curNode->children.find(ch) == curNode->children.end()){
                return false;
            } 
            curNode = curNode->children[ch];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
