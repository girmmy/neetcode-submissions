from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for letter in s:
            hashmap1[letter]+=1
        
        for letter in t:
            hashmap2[letter]+=1

        if hashmap1 == hashmap2:
            return True

        return False