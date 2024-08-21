class Solution:
    def numberToWords(self, num: int) -> str:
        trad = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        trad_2 = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        def smallnum2words(num):
            answer = ""
            if num == 0:
                return "Zero"
            if num>=100:
                cent = num//100
                answer = f"{trad[cent]} Hundred"
            num = num%100
            if num == 0:
                return answer
            if num<=19:
                answer += f" {trad[num]}"
            else:
                answer += f" {trad_2[num//10]}"
                if num%10 != 0:
                    answer += f" {trad[num%10]}"
            return answer if answer[0]!= " " else answer[1:]

        total_answer = ""
        if num==0:
            return "Zero"
        if num>=10**9:
            total_answer += f"{smallnum2words(num//10**9)} Billion"
            num = num%10**9
        if num>=10**6:
            num_millions = smallnum2words(num//10**6)
            total_answer += " " + num_millions+ " Million"
            num = num%10**6
        if num>=10**3:
            num_thousands = smallnum2words(num//10**3)
            total_answer += " " + num_thousands+ " Thousand"
            num = num%10**3
        if num>=1:
            total_answer+= " "+smallnum2words(num)
        return total_answer if total_answer[0]!= " " else total_answer[1:]





        