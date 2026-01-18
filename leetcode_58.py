class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sent=s.strip()
        words=sent.split()

        return len(words[-1])

