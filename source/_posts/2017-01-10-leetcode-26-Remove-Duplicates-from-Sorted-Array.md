---
title: '[leetcode]26. Remove Duplicates from Sorted Array'
date: 2016-09-10
tags: leetcode
---
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

```JavaScript
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var quickSort = (nums,left,right)=>{
        if(left>=right){
            return;
        }else{
            let base = nums[left],low=left+1,high=right,curIndex=left;
            while(low<high){
                while(low<high && nums[high]>=base){
                    high--;
                }
                while(low<high && nums[low]<=base){
                    low++;
                }
                nums[curIndex]=nums[high];
                nums[high]=nums[low];
                curIndex = low; 
            }
            nums[curIndex]=base;
            quickSort(nums,left,curIndex);
            quickSort(nums,curIndex+1,right);
        }
    };
    let count = 0;
    for(let i=1;i<nums.length;i++){
        if(nums[i]===nums[i-count-1]){
            count++;
        }else{
            nums[i-count] = nums[i];//把后面的向前移动count位
        }
    }
    return nums.length-count;
};
```

### 分析
做此题时，没读清题目中的先决条件——已排序数组，顾前大半段时间用来了复习快速排序，不过也是有所收获啦，查到阮一峰的博客里面的快速排序竟然不是原地排序，而看了几个其他的实现都与我印象最深的不太一样，就自己摸索着实现了一遍：
#### 原地快速排序的思路
取待排序数组的第一个元素为基准元素，将其取出保存到base中，并记这个空位置为curIndex。然后从数组最后一个位置开始向前寻找到第一个比基准值小的元素，此时其位置是high，接着从数组最左边向后寻找到第一个比基准值大的元素，或者到与high坐标相遇停止。
这个时候，high处的值赋给curIndex处的值，low处的值赋给high处的值，原low处便空出来成为了新的空位置。直到最后low==high，low还是一个空位置，这时候把基准值填上去，便实现了基准值左边全是更小的数值，基准值右边全是更大的数值了。
然后递归调用该函数。（注意！）但这时候关键问题来了，我们必须不能忘记边界值和结束情况：要在函数的一开始进行判断，如果数组只有一个元素，就不进行任何操作了。

#### 已排序数组移除重复元素
这才是这题要考察的，思路是：遍历一遍数组，当发现当前元素与它前面的非空元素值相等时，便把它置空；不相等时，便把它向前移动空元素的个数的距离。用一个count来记录空元素个数。


