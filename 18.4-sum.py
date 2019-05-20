#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ln = len(nums)
        ret = []
        for i in range(ln-3):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, ln-2):
                if j != i+1 and nums[j]==nums[j-1]:
                    continue
                m = j+1
                n = ln-1
                temptarget = target - nums[i] - nums[j]
                #print nums, i, j, m, n, temptarget
                while m < n:
                    if nums[m] + nums[n] > temptarget:
                        n-=1
                    elif nums[m] + nums[n] < temptarget:
                        m+=1
                    else:
                        ret.append([nums[i],nums[j],nums[m],nums[n]])
                        m+=1
                        while m<n and nums[m]==nums[m-1]:
                            m+=1
                        n-=1
                        while m<n and nums[n]==nums[n+1]:
                            n-=1
        return ret
                
        

