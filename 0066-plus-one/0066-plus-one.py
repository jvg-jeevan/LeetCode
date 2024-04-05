class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for i in digits:
            nums += str(i)
        # convert the list of numbers to a string
        num = int(nums) + 1
        # add 1 to the num to get plus one
        
        # list1 = []
        # take an empty list to store result
        # while num > 0:
        #     # add indivisual digit to list
        #     rem = num % 10
        #     num //= 10
        #     list1.append(rem)
        # reverse the list beacuse it starts from right
        # list1.reverse()

        return list(map(int, str(num)))
        # convert the number of string and then convert each digit to int and add that to list1 and return