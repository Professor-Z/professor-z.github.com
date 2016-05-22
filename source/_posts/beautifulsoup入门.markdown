---
layout: post
title: beautifulsoup入门
date: 2014-03-27
tags: python
categories: 编程语言 
---
先贴上代码，再详细的写一下在写这些代码的过程中遇到的问题，解决的方法。

<!--more-->
```python
#coding:utf-8
'''
Created on 2014年3月20日

@author: ZSH
'''
import urllib.request
import json
from bs4 import BeautifulSoup
import os
import time

 
def get_data(code):
    codestr = str(code)
    d1 =[]#一个列表存一条记录
    for year in range(1990,2015):
        yearstr = str(year)
        for season in range(1,5):
            jidu = str(season)
            url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/'+codestr+'.phtml?year='+yearstr+'&jidu='+jidu
            rsp = urllib.request.urlopen(url)
            html = rsp.read()
            soup = BeautifulSoup(html, from_encoding = 'GB2312')
            tablesoup = soup.find_all('table', attrs = {'id':'FundHoldSharesTable'}) 
            try:
                rows = tablesoup[0].findAll('tr')
            except:
                continue
            for row in rows[2:]:
                data = row.findAll('td')               
                d2 = {}
                d2['stock_id'] = code
                d2['release_date'] = data[0].get_text(strip = True)
                d2['open'] = data[1].get_text(strip = True);
                d2['high'] = data[2].get_text(strip = True);
                d2['close'] = data[3].get_text(strip = True);
                d2['low'] = data[4].get_text(strip = True);
                d2['volume'] = data[5].get_text(strip = True);
                d2['amount'] = data[6].get_text(strip = True);
                d1.append(d2);
    encodejson = open('DATA/' + code+'.json','w')
    encodejson.write(json.dumps(d1,indent=2,ensure_ascii = False))
#     encodejson.write(strfile)

def get_stocklist():
    stockf = open('DATA/log/stockid.txt','r')
    stocklist = []
    for ln in stockf.readlines():
        stocklist.append(ln.strip('\n'))
    return stocklist

if __name__ =='__main__':
    stocklist = get_stocklist()
    newpath = 'DATA/ '
    logpath = 'DATA/log/ '
    os.makedirs(newpath,exist_ok = True)
    os.makedirs(logpath,exist_ok = True)
    logtxt = open(logpath +'log.txt','w')
    for i in range(0,len(stocklist)):
        get_data(stocklist[i])
        stri = str(i)
        strlen = str(len(stocklist))
        print('已完成'+strlen+'条数据中的'+stri+'条！')
        print(time.strftime('%X',time.localtime() ))
        logtxt.write('已完成'+strlen+'条数据中的'+stri+'条！\n')
        logtxt.write(time.strftime('%X',time.localtime() ))
```




1. windows下，Python环境的搭建，我的环境是myeclipse+pydev，参考的教程帖子是Python环境搭建 个人觉得myeclipse是个非常强大的编译器，上手较容易。关于Python函数，for 语句等等基本基本语法，我推荐两个文档，一是“Python简明教程”（中文），内容通俗易懂。另一个就是位于C:\Python34\Doc的说明文档。

2. 这个脚本用到的第三方模块——beautifulsoup4，也就是from bs4 import BeautifulSoup 这一句代码牵扯到的，这个模块用于从html代码中分析出表格区域，进一步解析出数据。关于beautifulsoup的安装我参考的是Windows平台安装Beautiful Soup 。

3. 关于用urllib.request模块实现整个功能的部分，我从这位大哥的博客里学到了好多，他的博客真是超级详细易懂，体贴初学者。博客地址

4. Python字符串“格式化”——也即替换句子中的某一个字符串。Python中与字符串相关的各种操作Python基础教程笔记——使用字符串 中讲的很详细。

5. Python2到Python3的转换，由于字符编码的问题（中文print出来是ascii码），有人建议换到Python3，因为Python3默认是utf-8，Python3.x和Python2.x的区别  这个链接讲了Python2和Python3的区别。