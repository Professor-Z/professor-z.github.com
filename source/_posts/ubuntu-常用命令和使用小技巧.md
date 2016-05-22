title: "ubuntu 实用工具"
date: 2015-10-06 20:37:23
tags: linux
---

正式切换到全ubuntu系统的状态已经好几天了，几乎没有（当然是有一些）很不方便又解决不了的，必须用windows的问题。在这里记录一下切换到ubuntu之后，为了方便使用所做的一些配置。
<!--more-->
###shadowsocks-qt5+shadowsocks帐号
现阶段（2015/10）shadowsocks还是一个科学上网（翻越中国网络防火长城访问google等网站）的利器，买一个￥5/月的帐号（买帐号邮件联系我），就能同时让你的PC/MAC/Android设备无障碍浏览Internet，感受自由冲浪的感觉～
跑题了，ubuntu下面使用shadowsocks客户端，我使用的还是有界面的。
安装过程，输入下面地命令即可，仅支持ubuntu14.04或更高版本。
```shell
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```
其他平台及官方文档点击[这里][2]。
安装后亲测可翻，如下图所示。
![翻墙成功效果][3]

###小鹤双拼输入法
由于个人习惯，以及从效率上讲双拼输入法确实比全拼稍微快一点。我一直在所有设备上用小鹤双拼。现在在ubuntu下面通过设置也可以使用双拼。
通过卸载自带的ibus输入法，然后安装fcitx输入法即可。过程参考百度经验一篇帖子，点击[这里][4]。
使用效果如下图。
![小鹤双拼挺好用的][5]

###其它无需配置即可使用的好工具
1. chrome浏览器
从官网上下载安装包，安装好，然后登录帐号（需要翻墙），chrome会自动地同步你的书签和扩展程序等。
2. Transmission Bittorrent 客户端
这是ubuntu（版本14.04）自带的一个BT客户端，可用性不输utorrent。



###更新日志
2015/10/6 完成ss介绍，小鹤双拼介绍，其它工具介绍。

  [1]: http://ww3.sinaimg.cn/mw690/6f6caab3jw1ewruhn60mlj202z02ejra.jpg
  [2]: https://github.com/shadowsocks/shadowsocks-qt5/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97
  [3]: http://ww1.sinaimg.cn/large/6f6caab3jw1ewruhnip1tj211y0lc784.jpg
  [4]: http://jingyan.baidu.com/article/1e5468f9288a06484861b767.html
  [5]: http://ww4.sinaimg.cn/large/6f6caab3jw1ewruyqq7vdj206502y3yr.jpg