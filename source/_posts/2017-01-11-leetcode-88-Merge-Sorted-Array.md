---
title: "[leetcode]88. Merge Sorted Array"
date: 2016-09-11 23:08:27
tags: leetcode
---
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#### Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Subscribe to see which companies asked this question

```
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // nums1.splice(m,nums1.length);
    // nums2.splice(n,nums2.length);
    // nums1.push(...nums2);
    // nums1.sort((a,b)=>a-b);
    while(n>0){
        nums1[m+n-1] = (m===0||nums2[n-1]>nums1[m-1])?nums2[--n] : nums1[--m]
    }
    
};
```

### 思路
两者拼接然后排序肯定是最low的方法，不过竟然AC了，2333.
感觉本题还是考察，原地操作的相关思路，题目中已给提示，所以就要从m+n-1处重新码一遍，就可以了，如果硬要从头排，要进行很多移动，思路不对。