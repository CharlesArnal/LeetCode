class Solution:
    def reorderSpaces(self, text: str) -> str:
        n_space = text.count(" ")
        words = text.split()
        n_words = len(words)
        if n_words == 1:
            return words[0]+" "*n_space
        space_per_word = floor(n_space/(n_words-1))
        add_space_at_end = n_space-(n_words-1)*space_per_word
        new_text = words[0]
        for word in words[1:]:
            new_text = new_text+" "*space_per_word+word
        return new_text+" "*add_space_at_end
        
        