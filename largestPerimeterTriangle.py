class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) == 3 and ((nums[0] + nums[1] > nums[2]) or (nums[0] + nums[2] > nums[1]) or (nums[1] + nums[2] > nums[0])):
            return nums[0] + nums[1] + nums[2]
        ans = []
        nums.sort()
        for i in reversed(range(2,len(nums))):
            if nums[i] < nums[i-1] + nums[i-2]:
                ans.append(nums[i] + nums[i-1] + nums[i-2])
        if ans:
            return max(ans)
        return 0