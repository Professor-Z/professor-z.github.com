---
title: vuuihc ARTS WEEK3
tags: ARTS
date: 2019-05-27 20:00:00
---
每周至少:
1.做一个 leetcode 的算法题
2.阅读并点评至少一篇英文技术文章
3.学习至少一个技术技巧
4.分享一篇有观点和思考的技术文章
<!--more-->
## Algorithm
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
总体思路是采用二分法找到分界点，将数组分为有序的两部分。
然后跟据目标值和临界值的想对大小，选择其中一部分，进行二分查找。
主要考察的是思路和边界条件的判断。
```

``` python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        if end < 0:
            return -1
        max_index = self.get_max_index(nums,start,end)
        #print max_index
        if nums[start] > target:
            return self.bis(nums,target, max_index+1, end)
        else:
            return self.bis(nums,target,start,max_index)
        
    def get_max_index(self, nums, start, end):
        if start >= end:
            return start
        mid = (start + end)/2
        if nums[mid] >= nums[mid-1] and nums[mid] >= nums[mid+1]:
            return mid
        elif nums[mid] >= nums[start]:
            return self.get_max_index(nums, mid+1, end)
        else:
            return self.get_max_index(nums, start, mid)
        
    def bis(self, nums, target, start, end):
        if start >= end:
            if nums[end] == target:
                return end
            else:
                return -1
        mid = (start + end)/2
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            return self.bis(nums,target,start,mid)
        else:
            return self.bis(nums,target,mid+1,end)
        
```
