class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        cur = 0
        i = 0
        
        while i<len(abbr):
            #print(f"i {i}, cur {cur}")
            if cur>=len(word):
                print("false 1")
                return False
            if not abbr[i].isnumeric():
                if abbr[i] != word[cur]:
                    print("false 2")
                    return False
                i += 1
                cur += 1
            elif abbr[i].isnumeric():
                if abbr[i] == "0":
                    return False
                num = ""
                while i< len(abbr) and abbr[i].isnumeric():
                    num+=abbr[i]
                    i+=1    
                num = int(num)
                cur += num
                if cur>len(word):
                    print("false 3")
                    return False
                print(f"cur {cur} num {num}")
        if cur<len(word):
            print("false 4")
            return False

        return True
        