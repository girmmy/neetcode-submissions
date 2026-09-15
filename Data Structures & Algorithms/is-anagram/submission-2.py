class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = collections.defaultdict(int)
        hashmap2 = collections.defaultdict(int)

        for letter in s:
            hashmap[letter] += 1
        
        for letter in t:
            hashmap2[letter] += 1

        if hashmap == hashmap2:
            return True
        else:
            return False
        
        