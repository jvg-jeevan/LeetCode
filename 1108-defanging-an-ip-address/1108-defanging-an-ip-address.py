class Solution:
    def defangIPaddr(self, address: str) -> str:
# approach 1
#         return address.replace('.', '[.]')
# # replace(old, new) is used to replace all the occurrences of the old to new 

# # approach 2
#         return '[.]'.join(address.split('.'))
# # split() the string to list at separator '.' then join the list elements with [.]

# approach 3
        result = ''
        for char in address:
            if char == '.':
                result += '[.]'
            else:
                result += char
        return result
# create a variable result to store the result string iterate through the string address and if char is '.' then add '[.]' to result or else add the char

