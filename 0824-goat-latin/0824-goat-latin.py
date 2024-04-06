class Solution:
    def toGoatLatin(self, sentence: str) -> str:
# split the string to list
        sentence = sentence.split()

# go according to the condition
        res = []
        for i in range(len(sentence)):
            # if vowels then 
            if sentence[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                res.append(sentence[i] + 'ma' + 'a'*(i+1))

            # if consonants
            else:
                res.append(sentence[i][1:]+sentence[i][0]+'ma'+'a'*(i+1))
        
        return ' '.join(res) 
# convert the list to string and return res