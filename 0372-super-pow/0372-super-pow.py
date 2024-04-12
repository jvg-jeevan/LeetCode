class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # convert b from list to num by mapping each digit to str and then joining and converting back to int
        return pow(a ,int(''.join(map(str, b))), 1337)