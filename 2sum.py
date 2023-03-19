class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        iterations=0
        for i in range(length):
            iterations+=i

        for i in range(iterations):
            if ((i == iterations-1) and (nums[i-1] + nums[i] == target) and length > 2):
                return [i-1, i]
            if nums[i] + nums[i+1] == target:
                return [i, i+1]
            