---
layout: post
title: 初识beautifulsoup
date: 2014-04-28 22:34:34
tags: python
categories: 编程语言
---
今天上午在电脑上把《Python简明教程》大略看完了，对Python的基本语法和用法熟悉了一些。

下午开始看beautifulsoup，用http://kevinkelly.blog.163.com/blog/static/21390809320133185748442/ 这个教程安装成功（自从把Python路径加到环境变量里面，觉得开发环境好用了许多，好吧是我之前太菜，其实还因为之前我看的笨办法学Python里面好像就没有说环境变量啥的，因为他是用powershell，看来..还是多找好书的问题）。
<!--more-->
然后在学习Python和beautifulsoup的时候，发现看官方文档确实也不太难，而且Python这种语言的那些库非常好用。
下午，我主要实现了以下代码：
```python
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
url='http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/600000.phtml'
page = urllib2.urlopen(url)
html = page.read()

soup = BeautifulSoup(html)
table =  soup.find(id = 'FundHoldSharesTable')
print table
page2 = open(r"C:\Users\你的用户名\Desktop\new.txt",'w')
page2.write(str(table))
```
这段代码做的事情就是先用urllib2库抓去了新浪财经上浦发银行的股票价格历史信息，然后把提取出来的网页源代码元beautifulsoup处理了一下，把价格等信息写到一个桌面上的文本文档中。

把beautifulsoup的官方文档存下来了，继续加油了。

感觉大二我学Python时，一学期看了那一本《笨办法学Python》，学到的东西跟这几天看《Python简明教程》学到的差不多。看来学东西，有一本好书、按合适的节奏看完那本书确实非常重要。但是，找到好书、采用科学的方法读是不容易做到的，是需要加以重视的——可以多泡泡图书馆、相关网站、相关论坛从而找到好书，读书时排除干扰，采取不同的读书策略（粗精结合，做笔记），适时应用。

对于做事情的心理，现在有的时候比较没有耐心和动力。但是偶尔还是能看到一些东西，让我想去奋斗去争取，像是点燃我的热血。我想，还是要趁着年轻，多给自己希望，多多加油，也许老的时候，感动自己的不是那些奉为真理的愿景，而是自己充实的生活。

晚上回来，因为看了一天电脑屏幕，电脑屏幕又小，故特别累，去图书馆呆了一晚上，看知乎上一些大牛的经历和回答，还是很厉害的，比如catchen。真是得加油啊。