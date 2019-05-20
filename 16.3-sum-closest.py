#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = target
        import sys
        diff = sys.maxsize
        for i1 in range(len(nums)-2):
            i2=i1+1
            i3=len(nums)-1
            while i2 < i3:
                tmp=nums[i1] + nums[i2] + nums[i3]
                if tmp > target:
                    if tmp - target < diff:
                        diff = tmp-target
                        ret = tmp
                    i3-=1
                elif tmp < target:
                    if target - tmp < diff:
                        diff = target - tmp
                        ret = tmp
                    i2+=1
                else:
                    return target
        return ret

        

