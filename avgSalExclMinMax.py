class Solution:
    def average(self, salary: List[int]) -> float:
        max = salary[0]
        min = salary[0]
        sum = 0
        for i in range(len(salary)):
            if salary[i] > max:
                max = salary[i]
            if salary[i] < min:
                min = salary[i]
            sum += salary[i]
        sub = min + max
        avg = (sum - sub) / (len(salary) - 2)
        return avg