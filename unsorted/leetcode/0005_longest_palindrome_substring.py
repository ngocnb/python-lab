class Solution:
    def longestPalindromeBruteForce(self, s: str) -> str:
        max_length = 0
        result = ""
        for i in range(len(s)):
            substr = s[i:]

            for j in range(len(substr)):
                temp = substr if j == 0 else substr[:-j]
                if temp == temp[::-1]:
                    if max_length < len(temp):
                        max_length = len(temp)
                        result = temp

                    break

        return result

    def longestPalindromeExpandAroundCenter(self, s: str) -> str:
        n = len(s)

        if s == "":
            return ""

        max_length = 1
        result = s[0]

        for i in range(n):
            temp = self.expandAroundCenter(s, i, i)
            if max_length < len(temp):
                max_length = len(temp)
                result = temp

            if i + 1 <= n - 1:
                temp = self.expandAroundCenter(s, i, i + 1)
                if max_length < len(temp):
                    max_length = len(temp)
                    result = temp

        return result

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    def longestPalindromeDynamicProgramming(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        max_length = 1
        result = s[0]

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and length > max_length:
                        max_length = length
                        result = s[i : j + 1]

        return result
