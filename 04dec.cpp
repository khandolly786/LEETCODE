class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i, j = 0, 0  # Pointers for str1 and str2
        
        while i < len(str1) and j < len(str2):
            # Check if characters match directly or after a single increment
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Move pointer for str2 if a match is found
            i += 1  # Always move pointer for str1
        
        # If we have matched all characters in str2, it is a subsequence
        return j == len(str2)
