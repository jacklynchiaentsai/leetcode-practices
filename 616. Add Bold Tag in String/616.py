"""
- use list of boolean to keep track of index intervals
- modify string index with insert -> use list -> join
- avoid overlapping just mark entire interval
n = len(s), m = len(words), k = avglen(word)
time: O(m * (n*k) * (n-k)) = O(m * (n^2 * k - n * k^2))
space: O(n)

"""
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bolded = [False] * len(s)

        for word in words:
            cur_index = s.find(word)
            while cur_index != -1:
                for i in range(cur_index, cur_index + len(word)):
                    bolded[i] = True
                cur_index = s.find(word, cur_index+1)
                
        print(bolded)    
        start_tag = "<b>"
        end_tag = "</b>"

        return_list = []
        for i in range(len(bolded)):
            if bolded[i] and ( i==0 or (not bolded[i-1])):
                return_list.append(start_tag)

            return_list.append(s[i])

            if bolded[i] and ( i == len(bolded) - 1 or (not bolded[i+1])):
                return_list.append(end_tag)

        return "".join(return_list)
            

            

            
            

