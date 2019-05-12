---
title: vuuihc ARTS WEEK1
tags: ARTS
date: 2019-05-12 20:00:00
---
每周至少:
1.做一个 leetcode 的算法题
2.阅读并点评至少一篇英文技术文章
3.学习至少一个技术技巧
4.分享一篇有观点和思考的技术文章
<!--more-->
## Algorithm
1. 给定一个数组，返回对于数组每一位，它后面的所有数里面最大的那个，最后一位输出-1。要求：空间复杂度O(1)，即in-place，无返回值。例[16,17,3,4,5,2]返回[17,5,5,5,2,-1]。
```
# 动态规划dp[i]=max(dp[i+1],nums[i+1])并把空间压缩到in-place
def right_max(nums):
  N=len(nums)
  for i in range(N-1,-1,-1):
        if(i==N-1):
            temp=-1
        else:
            nums[i]=max(nums[i+1],temp)
        nums[i],temp=right_max,nums[i]
  return nums
```

## Review
在 GO 语言中创建你自己的 OAuth2 服务：客户端凭据授权流程
原文：https://hackernoon.com/build-your-own-oauth2-server-in-go-7d0f660732c3
译文：https://juejin.im/post/5c77639a5188251fd46eea45

拓展：SSO、CAS、oauth2的区别是什么？
回答：首先，CAS 是耶鲁大学实现的一个SSO实现方案。
其次，OAUTH是一个授权协议，SSO是描述『通过一个站点的凭证访问多个不同域名网站』场景的高级概念。
```
To Start, OAuth is not the same thing as Single Sign On (SSO). While they have some similarities — they are very different. OAuth is an authorization protocol. SSO is a high-level term used to describe a scenario in which a user uses the same credentials to access multiple domains.
```

## Tip
问题：vim 中，如何在行内快速跳转？
答案：除了 w,b,0,$，可以尝试插件 `Lokaltog/vim-easymotion`,`,, + w/h/l/j/f`

## Share
golang 的并发实现原理。

https://cloud.tencent.com/developer/article/1069239
https://www.zhihu.com/question/20862617