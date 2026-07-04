class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        s = set(nums)
        for i in range (len(nums)):
            t = target - nums[i]
            if t in s:
                for j in range (i+1, len(nums)):
                    if nums[j] == t:
                        return [i,j] 

        return answer
        