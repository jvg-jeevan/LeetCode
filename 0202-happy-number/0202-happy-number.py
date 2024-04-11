class Solution:
    def isHappy(self, n: int) -> bool:
    # visit is a set to store visited number
        visit = set()
    # while n not equal to 1
        while n != 1:
# if number is already in visit then number is False beacuse repeated number results in same result
            if n in visit:
                return False
            # if n not in visit add n to set(visit)
            visit.add(n)
        # to get the sum of squares of digits and assign the same to n
            n = sum(int(i)**2 for i in str(n))
    # if num becomes 1 then return True
        return True