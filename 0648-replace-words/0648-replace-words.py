class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
# split the str sentence to list of words
        sentence = sentence.split()

# for each word in sentence 
        for i in range(len(sentence)):
# if the word starts with element in dictionary then replace word with element
            for word in dictionary:
                if sentence[i].startswith(word):
                    sentence[i] = word
# return in str format
        return ' '.join(sentence)