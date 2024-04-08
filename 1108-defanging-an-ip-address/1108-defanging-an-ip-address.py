class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
# replace(old, new) is used to replace all the occurrences of the old to new 