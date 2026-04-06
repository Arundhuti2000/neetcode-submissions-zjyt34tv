class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_final = defaultdict(list)
        for string in strs:
            freq_count= [0]*26
            for i in string:
                freq_count[ord(i)-ord('a')]+=1
            anagram_final[tuple(freq_count)].append(string)
        return list(anagram_final.values())