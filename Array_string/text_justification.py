class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """ 
        First part: Break down words into list of lists by ensuring all words fit with at least 1 space in between, for each row

        Second part: Distribute space among each list inside the ans list 
        For rows with only one word or the last row, make them left-justified (Add 1 space in between, then add space to fill the remaining) 
        For others, generate a spaces list first, then add space to each word except the last 
        """ 

        ans = [] 
        cur = [] 
        curlen = 0 

        for w in words: 
            if curlen == 0: 
                curlen += len(w) 
            else: 
                curlen += 1+len(w)  # 1 for the space 
            
            if curlen > maxWidth: 
                ans.append(cur) 
                cur = [w]
                curlen = len(w) 
            else: 
                cur.append(w) 
        
        # add the last one 
        if cur: 
            ans.append(cur) 

        # -------------------------------------------------------------------------
        # distribute space 
        for i in range(len(ans)): 
            # if ans[i] only has one word, make it left-justified 
            if len(ans[i]) == 1: 
                ans[i] += ' '*(maxWidth-len(ans[i][0]))
                ans[i] = ''.join(ans[i])
                continue 
            
            # if i is the last row, make it left-justified 
            if i == len(ans)-1: 
                ans[i] = ' '.join(ans[i])
                ans[i] += ' '*(maxWidth-len(ans[i]))
                continue 

            number = len(ans[i])-1  # number of space areas to be added 
            spaces = [0 for _ in range(number)]

            rem = maxWidth - sum(len(w) for w in ans[i])
            for j in range(number): 
                spaces[j] = rem//number
            
            if number: 
                for j in range(rem % number): 
                    spaces[j] += 1 
            
            # add the spaces HERE 
            spaces.append(0)  # the last word have no ending space 
            for k in range(len(ans[i])): 
                ans[i][k] += ' '*spaces[k]

            ans[i] = ''.join(ans[i])

        return ans 

                
