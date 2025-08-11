class Solution:
    def reverseWords(self, s: str) -> str:
        """ 
        use a cur string to maintain the current word, 
        and append it to front of ans when cur == ' '. 
        finally add the cur if it is not empty. 
        """ 

        ans = "" 
        
        # trim s
        s = s.strip() 

        cur = ''
        i = 0 
        for i in range(len(s)): 
            if s[i] == ' ': 
                # only append when cur != '' to prevent adding multiple spaces 
                if cur != '':
                    ans = cur + ' ' + ans 
                    cur = ''
            else: 
                cur += s[i]
        
        ans = cur + ' ' + ans 
        return ans[:-1]
