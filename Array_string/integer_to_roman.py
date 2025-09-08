class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Constraints: 1 <= num <= 3999
        Based on thne constraints, we can hardcode the values based on each number position below 
        """ 

        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

        # extract the digits from the num (Without converting to string) 
        a = num//1000 
        b = (num%1000)//100 
        c = (num%100)//10
        d = num%10

        return thousands[a] + hundreds[b] + tens[c] + ones[d]
