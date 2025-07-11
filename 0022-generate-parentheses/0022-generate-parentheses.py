class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        para =[]
        
        def backT(s ="", open = 0, close = 0):
            if len(s) == 2*n:
                para.append(s)
                return
            if open<n:
                backT(s+"(",open+1, close)
            if close < open:
                backT(s+")",open,close+1)

        backT()     
        return para    
        