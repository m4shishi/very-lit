class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        temp = n
        count = 0
        while temp > 0:
            temp = temp // 10
            count += 1
        if count == 1:
            return 0
        for i in range(count):
            prod = prod * (n % 10)
            sum = sum + (n % 10)
            n = n // 10
        return prod - sum