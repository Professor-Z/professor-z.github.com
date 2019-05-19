---
title: vuuihc ARTS WEEK2
tags: ARTS
date: 2019-05-19 20:00:00
---
每周至少:
1.做一个 leetcode 的算法题
2.阅读并点评至少一篇英文技术文章
3.学习至少一个技术技巧
4.分享一篇有观点和思考的技术文章
<!--more-->
## Algorithm
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
``` python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        newList = [newInterval]
        for inv in intervals:
            lastIntv = newList[-1]
            if self.need_merge(lastIntv, inv):
                lastIntv = self.merge(lastIntv, inv)
                newList[-1] = lastIntv
                continue
            elif lastIntv[0] > inv[1]:
                newList.insert(len(newList)-1, inv)
            else:
                newList.append(inv)
        return newList

    def need_merge(self, intv1, intv2):
        if intv1[0] > intv2[1] or intv1[1] < intv2[0]:
            return False
        return True
    
    def merge(self, intv1, intv2):
        return [min(intv1[0], intv2[0]), max(intv1[1], intv2[1])]
```

## Review

Has the Python GIL been slain?
https://hackernoon.com/has-the-python-gil-been-slain-9440d28fa93d

1. GIL 是一个锁，被cpython（解释器）使用，导致Python代码实际上是单线程的（虽然可以用threading，可以用async 方法，能提高代码运行效率）
```
The GIL, or Global Interpreter Lock, is a boolean value in the Python interpreter, protected by a mutex. The lock is used by the core bytecode evaluation loop in CPython to set which thread is currently executing statements.

CPython supports multiple threads within a single interpreter, but threads must request access to the GIL in order to execute Opcodes (low-level operations). This, in turn, means that Python developers can utilize async code, multi-threaded code and never have to worry about acquiring locks on any variables or having processes crash from deadlocks.
```
2. 多进程模块 multiprocessing 可以利用多核， 但是有很大的开销。
```
The multiprocessing has 1 major flaw. It has significant overhead, both in time and in memory usage. CPython startup times, even without no-site, are 100–200ms (see https://hackernoon.com/which-is-the-fastest-version-of-python-2ae7c61a6b2b).
```
2. PEP554 提议把interpreter放入标准库，从而使得利用多核更为方便。开销较小。预计在Python3.8到Python3.9中加入。

### 评价：为什么要和 golang 抢饭吃呢，能抢过吗。

## Tips
https://coderwall.com/p/cp5fya/measuring-execution-time-in-go
Measuring execution time in Go
```golang
func main() {
    start := time.Now()

    r := new(big.Int)
    fmt.Println(r.Binomial(1000, 10))

    elapsed := time.Since(start)
    log.Printf("Binomial took %s", elapsed)
}
```
## Share
https://juejin.im/post/5cdd285b6fb9a0321d73cff3
滴滴陶文：我眼中的技术深度

其实评委在问你技术深度的时候，并不是问你技术栈的深度（比如是否从像素渲染到硅的提纯都了然于胸），真正在问的是你的竞争力在哪里。

