class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

# check for equality of s and s
        return self.remove_backspace(s) == self.remove_backspace(t)

    
    def remove_backspace(self, string):
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
# if len(res) is zero then cannot delete element continue
                if len(res) == 0:
                    continue
# if elements are in res then remove the last element
                else:
                    res.pop()
# return res in form of str
        return ''.join(res)