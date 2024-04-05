class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        # create a set to add unique elements
        for i in nums:
            # if element is already in set return True i.e duplicate exists
            if i in set1:
                return True
            # if element is unique add that to set
            set1.add(i)
        # if all elements are unique return False
        return False