"""
Trie: search words of pattern 
time: 
    n = len(word)
    addWord: O(n)
    search: O(26^n)
space: 
    addWord: O(n)
    search: O(n) recursive stack
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.rootNode = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.rootNode
        for char in word:
            if char not in curNode.children:
                childNode = TrieNode()
                curNode.children[char] = childNode
            else:
                childNode = curNode.children[char]
            
            curNode = childNode
        
        curNode.isEnd = True

    def search(self, word: str) -> bool:
        def findMatchingWord(curIndex, curNode):
            curchar = word[curIndex]
            if curchar != '.':
                if curchar in curNode.children:
                    childNode = curNode.children[curchar]
                    if curIndex == len(word) - 1:
                        if childNode.isEnd == True:
                            return True
                        else:
                            return False
                    else:
                        return findMatchingWord(curIndex + 1, childNode)
                else:
                    return False

            else:
                for char, childNode in curNode.children.items():
                    if curIndex == len(word) - 1:
                        if childNode.isEnd == True:
                            return True
                    else:
                        if findMatchingWord(curIndex + 1, childNode):
                            return True

                return False 

        return findMatchingWord(0, self.rootNode)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
class TrieNode:
    children = {nextchar: TrieNode}
    isEnd = True if there is a word that ends in this TrieNode and otherwise false

init:
    rootNode: TrieNode(isEnd = True)
addWord:
    curNode: rootNode
    for char in word:
        if char not in curNode's children:
            create a child TrieNode
            update curNode.children[char] = childNode
        else:
            access the childNode

        curNode = childNode

    curNode.isEnd = True

search:
    return findMatchingWord(0, rootNode)
    def findMatchingWord(curIndex, curNode):
        if word[curIndex] != '.':
            if word[curIndex] in curNode,children:
                if curIndex == len(word) - 1:
                    if childNode.isEnd == True:
                        return True
                    else:
                        return False

                else:
                    if findMatchingWord(curIndex + 1, curNode.childNode):
                        return True
            else:
                return False
        else:
            for childNode in curNode.children:
                if curIndex == len(word) - 1:
                    if childNode.isEnd == True:
                        return True
                else:
                    if findMatchingWord(curIndex + 1, childNode):
                        return True

            return False
"""
