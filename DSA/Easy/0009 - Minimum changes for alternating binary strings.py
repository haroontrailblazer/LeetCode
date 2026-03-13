class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0
        
        for i in range(len(s)):
            if int(s[i]) != i % 2:
                changes += 1
        
        return min(changes, len(s) - changes)