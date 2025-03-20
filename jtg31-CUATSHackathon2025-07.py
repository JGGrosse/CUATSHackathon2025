class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==0:
            if len(t)==0:
                return True
            else:
                return True

        for letter in s:
            if s.count(letter) != t.count(letter):
                return False
        for letter in t:
            if s.count(letter) != t.count(letter):
                return False
        return True
