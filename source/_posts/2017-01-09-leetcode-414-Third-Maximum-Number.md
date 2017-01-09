---
title: '[leetcode]414. Third Maximum Number'
date: 2016-09-09 23:01:39
tags: leetcode array
---
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

#### Example 1:
```
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.
```
#### Example 2:
```
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
#### Example 3:
```
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

```JavaScript
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    var max=[];
    var placeNum = function(num){
        if(max.indexOf(num)===-1){
            max.push(num)
            max.sort(function(a,b){
                if(a>b)
                  return -1
                else
                  return 1
            })
            if(max.length>3)
                max = max.slice(0,3)
        }
    }
    for(var i=0;i<nums.length;i++){
        placeNum(nums[i])
    }
    if(max[2]!==undefined){
        return max[2]
    }else{
        return max[0]
    }
};
```
