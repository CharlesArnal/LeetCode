class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def w2greaterthanw1(word1, word2):
            i = 0
            while i<min(len(word1),len(word2)):
                if order.find(word1[i])>order.find(word2[i]):
                    return False
                elif order.find(word1[i])<order.find(word2[i]):
                    return True
                i+=1
            if len(word1)>len(word2):
                return False
            else:
                return True
        for i in range(len(words)-1):
            if not w2greaterthanw1(words[i],words[i+1]):
                return False
        return True


        