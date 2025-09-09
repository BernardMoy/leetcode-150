class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 
        The most simple backtracking form
        call recursive function on digits[1::]
        then append every possible digit letter to every previous result 
        """ 

        if not digits:
            return []
        
        letdict = {}
        letdict['2'] = 'abc'
        letdict['3'] = 'def'
        letdict['4'] = 'ghi'
        letdict['5'] = 'jkl'
        letdict['6'] = 'mno'
        letdict['7'] = 'pqrs'
        letdict['8'] = 'tuv'
        letdict['9'] = 'wxyz'

        # the use of this helper is to prevent redeclaration of let dict 
        def helper(digits): 
            # base case: convert the dict string into lists 
            if len(digits) == 1: 
                return list(letdict[digits[0]])
            
            # recursively call function on [1::]
            ans = [] 
            prev = helper(digits[1::])
            for let in letdict[digits[0]]: 
                for res in prev: 
                    ans.append(let+res)
            
            return ans 
        
        return helper(digits)