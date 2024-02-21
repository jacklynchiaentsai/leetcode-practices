"""
n: number of synonym words
m: length of text
w: number of words in text
worst: n^w synonymous sequences
time: O (n^w log (n^w) + n^2)
space: O(n^w + n)
"""
class Solution:
    def __init__(self):
        self.ans = None
    
    def findRep(self, word, rep_dic):
        if word not in rep_dic:
            rep_dic[word] = word
            return word
        else:
            if rep_dic[word] == word:
                return word
            else:
                return self.findRep(rep_dic[word], rep_dic)

    def mergeGroup(self, rep1, rep2, rep_dic, syn_group_dic):
        if rep1 == rep2:
            return None
        
        if rep1 not in syn_group_dic:
            syn_group_dic[rep1] = [rep1]
        if rep2 not in syn_group_dic:
            syn_group_dic[rep2] = [rep2]
        
        if rep1 < rep2:
            rep_dic[rep2] = rep1
            syn_group_dic[rep1].extend(syn_group_dic[rep2])
        else:
            rep_dic[rep1] = rep2
            syn_group_dic[rep2].extend(syn_group_dic[rep1])
    
    def genSeq(self, text_li, curIndex, rep_dic, syn_group_dic, syn_seq):
        if curIndex == len(text_li):
            self.ans.append(syn_seq[1:])
            return None
        
        word = text_li[curIndex]

        if word not in rep_dic:
           self.genSeq(text_li, curIndex+1, rep_dic, syn_group_dic, syn_seq + " " + word) 
        else:
            wordrep = self.findRep(word, rep_dic)
            syn_list = syn_group_dic[wordrep]
            for synonym in syn_list:
                self.genSeq(text_li, curIndex + 1, rep_dic, syn_group_dic, syn_seq + " " + synonym)

    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        self.ans = []
        rep_dic = {}
        syn_group_dic = {}

        for synonym in synonyms:
            word1 = synonym[0]
            word2 = synonym[1]
            rep1 = self.findRep(word1, rep_dic)
            rep2 = self.findRep(word2, rep_dic)
            self.mergeGroup(rep1, rep2, rep_dic, syn_group_dic)

        text_li = text.split()
        self.genSeq(text_li, 0, rep_dic, syn_group_dic, "")
        self.ans.sort()
        return self.ans
"""
each word would have a representative word 
rep_dic = {word: representative word}
syn_group_dic = {rep word: [synonym words]}

1. split by space
2. recursive maintaining a string of reproduced text
"""
