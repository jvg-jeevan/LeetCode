class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

# call the method for both the str s, t
        str1 = self.remove(s)
        str2 = self.remove(t)
        print(str1)
        print(str2)
# check for equality of str1 and str2
        return str1 == str2

    
    def remove(self, string):
        """Method checks for # (backspace) and removes the char if present"""
# res to store resultant list of chars
        res = []
# iterate through each char 
        for i in range(len(string)):
# if char != '#' append the char to res list
            if string[i] != '#':
                res.append(string[i])
# if char = '#' remove the last element i.e backspace deletes the char
            else:
# if len(res) is zero then cannot delete element
                if len(res) == 0:
                    continue
                else:
                    res.pop()
# return res in form of str
        return ''.join(res)
