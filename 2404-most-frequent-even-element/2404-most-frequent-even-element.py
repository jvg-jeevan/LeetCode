from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
# evens list contains only even elements
        evens = list(filter(lambda n: n%2 == 0, nums)) 

# res is dict() key= number, value= number of occurrences
        res = Counter(evens)

# res dict() is sorted() in decreasing order of value(number of occurrences) in increasing order of number(key)
        res = dict(sorted(res.items(), key= lambda items: (-items[1], items[0])))

# numbers contains list of keys
        numbers = list(res.keys())

# return -1 if numbers list is empty
        if not numbers:
            return -1
# return the top most element
        return numbers[0]