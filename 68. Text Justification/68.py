"""
n = len(words)
k = average length of a word
m = maxLength
time: O(n*k)
space: O(m) from join function
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # returns endIndex (inclusive): O(n)
        def getWords(startIndex):
            curWidth = 0
            curIndex = startIndex
            while curIndex < len(words):
                curWidth += len(words[curIndex]) + 1
                
                if curWidth > maxWidth + 1:
                    return curIndex - 1

                curIndex += 1
            
            if curIndex == len(words):
                return len(words) - 1
                
            return curIndex

        # print(getWords(6))

        # returns averageGap, additionalGaps
        def calcGap(startIndex, endIndex):
            curWidth = len(''.join(words[startIndex: endIndex + 1])) # O(n*k)
            remaining = maxWidth - curWidth

            if startIndex == endIndex:
                return remaining, 0
            
            numGaps = endIndex - startIndex
            averageGap =  math.floor(remaining / numGaps)
            additionalGaps = remaining % numGaps
            return averageGap, additionalGaps
        
        # startIndex = 6
        # print(calcGap(startIndex, getWords(startIndex)))

        def generatelastLine(startIndex, endIndex):
            line = ""
            for i in range(startIndex, endIndex + 1):
                line += words[i] + " "
            
            line = line[:maxWidth]
            line += " " * (maxWidth - len(line))
            return line

        def generateLine(startIndex, endIndex):
            averageGap, additionalGaps = calcGap(startIndex, endIndex)
            line = ""
            for i in range(startIndex, endIndex + 1):
                line += words[i]
                line += " " * averageGap

                if additionalGaps > 0:
                    line += " "
                    additionalGaps -= 1

            line = line[:maxWidth]
            return line

        # generate line
        results = []
        startIndex = 0
        while startIndex < len(words):
            endIndex = getWords(startIndex)
            line = None
            if endIndex == len(words) - 1:
                line = generatelastLine(startIndex, endIndex)
            else:
                line = generateLine(startIndex, endIndex)
            
            results.append(line)
            startIndex = endIndex + 1
        
        return results
"""
software engineering problem: modularity -> helper functions 
-> debugging by parts
test with edge cases
"""



