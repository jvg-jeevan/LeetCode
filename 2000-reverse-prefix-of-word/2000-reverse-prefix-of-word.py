class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
# convert the str to list
        word_list = list(map(str, word))
# if ch not in list then return word
        if ch not in word_list:
            return word
# if ch in list then get the index of the ch
        else:
            ind = word_list.index(ch)
# return the str() reverse the 1st part upto the ch and concatenate the other
        return word[ind::-1] + word[ind+1:]