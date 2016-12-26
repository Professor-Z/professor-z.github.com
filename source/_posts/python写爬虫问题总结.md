---
layout: post
title: python写爬虫问题总结
date: 2015-01-27
tags: python
---
### Python文件与idle关联
我在windows环境下开发Python时，一般用sublime text 2 写Python代码，用安装Python时自带的IDLE来调试。有时候安装程序并没有帮你绑定IDLE和`.py`文件。这时候，需要我们自己去绑定。
步骤：
1. 右击`.py`文件，选择打开方式
2. 选择`在这台电脑上选择应用程序`（我的是win8.1）
3. 选择你Python安装路径下的一个文件夹里面的`idle.bat`文件来打开。比如我的是在`C:\Python33\Lib\idlelib\idle.bat`
之后你就可以直接双击`.py`文件用IDLE打开，然后用F5，去运行并调试你写的程序了
<!--more-->
### IDLE提示缩进错误
出现这个错误的原因可能是，Python自带的IDLE的tab的缩进和你的编辑器（比如sublime text 2）的tab 默认缩进大小不同，而且IDLE本身它对space和tab是区分的。所以经常会出现虽然你视觉上感觉不到缩进有错误，但是执行程序的时候，IDLE会报错。
解决方法是这样的，在IELD中，选择菜单栏的Edit->Select ALL，然后选择菜单栏的Format->Untabify Region。就可以了。
这个做法的作用是，把所有的tab替换成了space。

### 在idle里面打印网页中文是乱码
windows系统下，用Python抓取网页时，在通过read()函数读取了网页之后，如果通过print打印出网页不经过编码转换，可能会出现网页中的中文字符以乱码的形式出现如下图所示。
这时的解决方法是，用gbk解码得到的网页。
把
```python
print(html)
```
改成
```python
print(html.decode("gbk"))
```
这个步骤的作用，是将以其它编码形式（一般是GBK）编码的中文解码成Unicode编码。
###爬虫进程超时阻塞
在程序的运行过程中，有时候会出现每隔一段时间（大约1小时），抓取就自动停止的bug，后来解决这个问题采用了引入socket模块并设置一个timeout值的方法来解决的，其中timeout值可以自定义，只要能解决自动停止这个bug即可。我在这个程序中设置了之后，程序假死的情况基本解决了。
```python
socket.setdefaulttimeout(50)
```
###单线程太慢

###sublime text 2编译任何语言控制台无输出

##更新日志
2015-7-1 更新“爬虫进程超时阻塞”