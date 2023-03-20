class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # c = 0
        # for i in range(low, high + 1):
        #     if i % 2 != 0:
        #         c += 1
        # return c
        count = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0:
            count += 1
        return count