class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        s = str(x)
        l = 0
        r = len(s) - 1
        result = True
        while l < r:
            if (s[l] != s[r]):
                result = False
                break
            
            l += 1
            r -= 1
        
        return result
    
    def isPalindromeReverseNumber(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]
    
    def isPalindromeMath(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        return x == reverted_number or x == reverted_number // 10