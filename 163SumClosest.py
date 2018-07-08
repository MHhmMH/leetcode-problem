class Solution(object):
    def threeSumClosest(self, nums, target):
        import numpy as np
        nums.sort()
        minsum = np.inf
        distance = np.inf
        for i in range (len(nums)):
            start = i+1 
            end = len(nums)-1
            while start < end:
                sumnow = nums[start] + nums[i] + nums[end] 
                if sumnow > target:
                    end -= 1
                if sumnow < target:
                    start += 1
                if sumnow == target:
                    return target
                if abs(target - sumnow) < distance:
                    minsum = sumnow
                    distance = abs(target - sumnow) 
        return minsum 