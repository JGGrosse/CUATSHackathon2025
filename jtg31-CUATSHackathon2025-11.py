class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for char in s:
            if char.islower() or char.isnumeric():
                new_s += char

        L = 0
        R = len(new_s) - 1

        if len(new_s) < 2:
            return True

        while L <= R:
            if new_s[L] != new_s[R]:
                return False
            L+=1
            R-=1
        return True
