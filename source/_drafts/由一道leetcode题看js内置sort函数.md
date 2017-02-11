---
title: 由一道leetcode题看js内置sort函数
tags: js
---
刷leetcode 时遇到了一道题目，题目内容很长，以至于难点主要在理解题意和抽象出思路来。题目摘抄如下：

%blockquote%
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
1. Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
2. Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
3. As long as a house is in the heaters' warm radius range, it can be warmed.
4. All the heaters follow your radius standard and the warm radius will the same.

### Example 1:
```
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
```
### Example 2:
```
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
```
%blockquote%

题目意思大致就是，在非负数数轴上，排列着一组房子，和一组加热站，要为所有的加热站配备同样的辐射半径（比如热水管道），让你求出最小辐射半径。
参考Top Solutions（划掉），得到一个思路，就是对于每个房子，求得它与最近的加热站的距离，然后对所有房子的最小加热距离取最大值即可。
最终，写出了可以AC的代码如下：
```
/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
var findRadius = function(houses, heaters) {
    //自定义一个二分查找函数
    var binarySearch = (array,key)=>{
        let left=0,right=array.length-1;
        while(left<right){
            let middle = left + ((right - left)>>1);
            if(array[middle] < key){
                left = middle + 1;
            }else if( array[middle] > key){
                right = middle - 1;
            }else{
                return middle;
            }
        }
        if(array[left]<key){
            return left+1;
        }
        return left;
    }
    heaters.sort((a,b)=>a-b);//对heaters数组排序
    let result =  -1;
    let max = 1e9;
    for(let i=0;i<houses.length;i++){//对于每一个房子
        let index = binarySearch(heaters,houses[i]);//得到它在heaters中的位置
        let dist1 = index>=1?houses[i]-heaters[index-1]:max;//得到与左边加热站（如果有）的距离
        let dist2 = index<heaters.length?heaters[index]-houses[i]:max;//得到与右边加热站（如果有）的距离
        result = Math.max(result,Math.min(dist1,dist2));//更新全局最大距离
    }
    return result;
};
```
这很好很不错。
但是，在AC之前，我遇到了一个情况，就是我用js写的quickSort函数来对heaters进行排序时，会在某些测试用例出现超时，而换成js内置的sort函数则可以通过。
这是为什么呢？
## js内置的sort函数不是封装好的用js写的排序函数吗？？？

答案可能是『不是』。
为了解开这个疑惑，我先Google了一下『js内置排序函数』，得到了仅有的一点信息是结果第一个的博文中提到『js内置排序函数混合使用了多重排序算法』，中文查询不行，那就换英文，搜索『js array sort』，几经跳转，进入了ecma-international.org/ecma-262/6.0/，开始看规范。
硬着头皮把规范里面关于Array.prototype.sort的部分大致看完，发现除了讲了一些使用规范（比如排序函数的定义），并没有讲sort函数用了什么算法。。

于是继续探究，Google『js array sort algorithm』终于找到了还算明白的解释：

js内置函数是由js引擎来实现的，因而不同的js引擎（浏览器内核）可能会有不同的实现方法，比如IE的排序算法是stable的，而Mozilla的则不是。
在stackoverflow的相关回答中，有人在参阅webkit源码后指出，根据数组的类型，Webkit使用了不同的排序方法，
1. 数字类型数组（或原始类型数组）使用C++标准库函数std::qsort进行排序，该函数是对快速排序一些变种后的实现。
2. 非数字类型的连续数组会先被字符串话，然后使用归并排序以获得稳定排序，如果归并排序不可用，就是用快速排序。
3. 对于其他类型（非连续数组，可能是关联数组），WebKit使用选择排序（他们称为“min”排序），或者在某些情况下，通过平衡二叉树排序。 不幸的是，这里的文档相当模糊，所以你必须查看源代码才能实际看到使用哪种类型的排序方法。

回到本文的题目上，我自己写的快排无法通过的原因大致就出来了，内置函数的排序过程是在js引擎内部，用C++语言执行，当然会比用js编译执行快很多啦。

参见：
http://www.ecma-international.org/ecma-262/6.0/#sec-array.prototype.sort
http://stackoverflow.com/questions/234683/javascript-array-sort-implementation
http://trac.webkit.org/browser/trunk/Source/JavaScriptCore/runtime/JSArray.cpp?rev=138530#L1124

