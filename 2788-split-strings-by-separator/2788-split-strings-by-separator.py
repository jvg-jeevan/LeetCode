class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
# result stores the elements split() by separator
        result = []
        for i in words:
            result.extend(i.split(separator))
# if the string element is empty then remove that element
        return [x for x in result if x != '']