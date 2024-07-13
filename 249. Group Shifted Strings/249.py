"""
dictionary with tabulation
n = len(strings) m = max(length of string in strings)
time: O(m*n)
space: O(m*n) // each string takes at most m space
"""
class Solution:
    def convertString(self, original_str):
        distance = ord(original_str[0]) - ord('a')
        converted_str = ""
        for char in original_str:
            chr_num = ord(char) - distance
            if chr_num < ord('a'):
                chr_num += 26
            
            converted_str += chr(chr_num)

        return converted_str

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group_map = {}
        conversion_map = {} #tabulation

        for string in strings:
            if string not in conversion_map:
                converted_str = self.convertString(string)
            else:
                converted_str = conversion_map[string]

            if converted_str not in group_map:
                group_map[converted_str] = []
            
            group_map[converted_str].append(string)
            conversion_map[string] = converted_str

        return group_map.values()
