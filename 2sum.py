class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length - 1 ):
            for j in range(i+1, length):
                if(nums[i] + nums[i+1] == target):
                    return [i, i+1]

#attempt 2, not inventing smtg new this time            