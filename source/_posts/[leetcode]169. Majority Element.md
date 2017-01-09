---
layout: post
title: [leetcode]169. Majority Element
date: 2015-09-26
tags: leetcode
---

Given an array of size n, find the majority element. The majority element is the element that appears more than  『n/2』 times.

You may assume that the array is non-empty and the majority element always exist in the array.

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        a = None
        count = 0
        for num in nums:
            if a==num:
                count+=1
            elif count==0:
                a=num
            else:
                count-=1
        return a
```
