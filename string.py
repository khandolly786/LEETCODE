class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            # Start counting occurrences of the current character
            count = 1
            while i + count < n and word[i] == word[i + count] and count < 9:
                count += 1
            
            # Append the count and the character to the result
            comp += str(count) + word[i]
            
            # Move the index forward by the count of characters processed
            i += count
        
        return comp
