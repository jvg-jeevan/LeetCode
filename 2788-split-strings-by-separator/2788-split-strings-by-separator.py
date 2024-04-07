class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
# result stores the elements split() by separator
        result = []
        for i in words:
            result.extend(i.split(separator))
# if the 
        return [result[x] for x in range(len(result)) if result[x] != '']