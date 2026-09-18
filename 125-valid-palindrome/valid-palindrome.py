class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Compare with reversed string
        return cleaned == cleaned[::-1]