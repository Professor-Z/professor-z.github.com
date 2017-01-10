---
title: '[leetcode]27. Remove Element'
date: 2017-01-10 22:19:56
tags:
---
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#### Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

```
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let count = 0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]===val){
            count++;
        }else{
            nums[i-count] = nums[i];
        }
    }
    return nums.length - count;
};
```

### 分析
与#26一样