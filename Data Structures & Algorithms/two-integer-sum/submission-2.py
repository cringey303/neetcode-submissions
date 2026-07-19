class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i in range(len(nums)):
            other = target-nums[i]
            if other in check:
                print(other)
                return [check[other], i]
            check[nums[i]]=i