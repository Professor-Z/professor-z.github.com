---
title: vuuihc ARTS WEEK4
tags: ARTS
date: 2019-06-24 20:00:00
---
每周至少:
1.做一个 leetcode 的算法题
2.阅读并点评至少一篇英文技术文章
3.学习至少一个技术技巧
4.分享一篇有观点和思考的技术文章
<!--more-->
## Algorithm
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.
```
思考一下题意，会发现这是一个求两个字符串最长公共子序列的问题。
最长公共子序列，暴力解法的复杂度是2^n
再回忆一下，这是动态规划的经典题目。
动态规划的特点？
1. 递推公式
2. 公式中，会使用一个（二维）数组记录中间结果

过程图解：
https://blog.csdn.net/hrn1216/article/details/51534607
```

``` python
def deletion_distance(str1, str2):
  cc = []
  l1, l2 = len(str1), len(str2)
  for i in range(l1+1):
    item=[]
    for j in range(l2+1):
      item.append(0)
    cc.append(item)
  #print cc
  ccs = []
  for i in range(1, l1+1):
    for j in range(1,l2+1):
      if str1[i-1]==str2[j-1]:
        cc[i][j] = cc[i-1][j-1] + 1
      else:
        cc[i][j] = max(cc[i-1][j], cc[i][j-1])
  i = l1
  j = l2
  while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
      if cc[i][j] > max(cc[i-1][j], cc[i][j-1]):
        ccs.append(str1[i-1])
        i-=1
        j-=1
    elif cc[i-1][j] > cc[i][j-1]:
      i-=1
    else:
      j-=1
  print ccs
  return l1+l2-2*cc[l1][l2]
  
        
```

## Review

http://brooker.co.za/blog/2019/04/03/learning.html
Learning to build distributed systems

文章是对『如何学习构建大型分布式系统』这一问题的回答，作者是亚马逊AWS的高级工程师。
主要内容要点如下：
1. 从别人成果中学习。
作者列举了大量的优秀学术论文，并提出，这些论文永远也看不完，关键是知道什么时候停止（个人理解是要知道看什么对自己是有用的）。

2. 上手去做。
作者建议自己动手去实现一个分布式系统，例如实现paxos, raft，并把过程中犯的错误记录下来。并提到golang的好处：写网络服务很方便，编译后也能到处去用。

3. 拓宽视野。
作者表示一些其他领域的知识，对解决现实问题可能也很有帮助，例如控制论、统计学等等。

4. owner 一个项目。
作者建议找到合适的机会，例如在亚马逊aws组，去owner一个项目并实现一个论文，对公司，同事和客户负责。并表示亚马逊的事故复盘机制能让人学到很多系统设计相关的东西。

5. 花上时间。
作者表示自己从事这个领域15年了，但是还是有种浮于表面的感觉，并表示学习新东西不是威胁，是机会。

## Tips

本周了解到一个模拟面试（英语）的网站，并第一次尝试了下，感觉效果非常棒！
网站具体用法是，你可以预约一个时间点，一般是一个小时。会给你一道题目，（可能根据面试主题内容不一样，这次我选的数据结构和算法，就给了一道算法题），类似leetcode的界面，你可以自己把这道题做出来，旁边有hints和answer，等面试开始，你就用这道题来考给你匹配的伙伴。
面试开始后，会用很短的时间给你匹配伙伴（本次给我匹配了几分钟，但是匹配了一个德国柏林的小姐姐），然后你们两个就开始自由聊天了，一般是两个人互相作为面试官和面试者进行模拟面试。具体过程各位自己可以去体验啦。
这里附上网址，用这个网址注册会有额外练习机会哦
https://www.pramp.com/invt/yB1d57n7q8HxaEQozmJZ


## Share
左耳朵耗子：如何超过大多数人
主要讲技术人员在认知上面的一些观点。前半段采用反讽的技巧的文字尤其出彩。
https://coolshell.cn/articles/19464.html
『好了，就这么多，如果哪天你变得消极和不自信，你要来读读我的这篇文章，子曰：温故而知新。』




