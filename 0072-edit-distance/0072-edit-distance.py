class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # dp[i][j] = min operations to convert word1[:i] → word2[:j]
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        # Base cases: one string is empty
        for i in range(1, m+1):
            dp[i][0] = i      # delete all i chars
        for j in range(1, n+1):
            dp[0][j] = j      # insert all j chars
        
        # Fill the table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],     # delete word1[i-1]
                        dp[i][j-1],     # insert word2[j-1]
                        dp[i-1][j-1]    # replace word1[i-1] → word2[j-1]
                    )
        
        return dp[m][n]
