class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        length = max_length = 0
        current_cutoff = -1
        for i in range(len(s)):
            char = s[i]
            if char not in char_dict:
                char_dict[char] = i
                length += 1
            else:
                matched_index = char_dict[char]
                if matched_index < current_cutoff:
                    char_dict[char] = i
                    length += 1
                else:
                    max_length = length if length > max_length else max_length
                    current_cutoff = matched_index
                    length = i - matched_index
                    char_dict[char] = i
        
        return max_length if max_length > length else length
