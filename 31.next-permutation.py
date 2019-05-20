#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        change = False
        for i in range(len(nums)-1):
            i = len(nums)-1-i
            for j in range(i):
                j = i-1-j
                if nums[j]<nums[i]:
                    # nums[i], nums[j] = nums[j], nums[i]
                    nums.insert(j, nums[i])
                    #print nums
                    del nums[i+1]
                    change = True
                    break
            if change:
                break
        if not change:
            return nums.reverse()
        return nums
        

