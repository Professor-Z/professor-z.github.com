---
title: '[leetcode]448. Find All Numbers Disappeared in an Array'
date: 2016-09-09 23:05:07
tags: leetcode array
---
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

#### Example:
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
94.7%
```JavaScript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    var result = Array.from({length:nums.length},(v,k)=>k+1)
    for(var i=0;i<nums.length;i++){
        result[nums[i]-1] = 0
    }
    return result.filter(item=>item!==0)
};
```
