---
layout: post
title: nodejs回调嵌套的思考
description: nodejs学习 nodejs入门 nodejs开发指南 nodejs回调嵌套 nodejs异步查询
date: 2014-05-21
categories: 编程语言
tags: node.js 学习总结
---
在学nodejs的过程中，我了解到的nodejs语法特性最突出的就是其单线程非阻塞特性。虽然在之前的入门手册中作者有讲这一方面，但是自己没实际用过还是不会。所以，在写我们的点菜系统的某一个“需要多次查询数据库然后统一返回结果”的函数的时候，一开始由于我对回调函数的使用不太熟悉，所以写出了并行查询的函数，结果出现每次查询还没返回数据就render网页的情况，也就导致网页上显示不出数据来。
<!--more-->
当时我的代码的结构是这样子的：
```javascript
function queryUser(req,res){
    ///一些初始化
    connection.query("SELECT * FROM database1",function(err,result){
    ///一些处理函数
    row1=result;
    });
    connection.query("SELECT * FROM database2",function(err,result){
    ///一些处理函数
    row2=result;
    });
    res.render('userProfile',{data1:row1,data2:row2});
}
```
这是一个查询个人信息的模块中的一个主要的功能函数，它从两个数据库里面查询出数据来，作为参数传到同一个前端页面。当然这是我本来希望它实现的功能，但实际的结果是每次都是返回空白，插入一些console.log打印出来也是空白的查询结果。后来，经过询问其他人，我才清楚了，在这个函数的执行过程中，两个查询在发出查询请求之后，才不会等着执行结果返回再执行下面的代码，这是同步编程才会做的事。它是发出查询之后接着向下执行，等到查询结果返回，再去执行回调函数。所以，往往都是先render了之后，查询结果才返回，所以才会出现那样的结果。
所以，怎么解决这个问题呢，就是把回调函数嵌套，也就是把第二个查询写在第一个查询的回调函数里面，把render写在第二个查询的回调函数里面，这样虽然在代码上结构上看两个查询，render似乎不像平等的顺序执行的样子，或者说代码有点奇怪，但是实际上，它确实是顺序执行的。修改后的实际代码如下：
```javascript
function queryUser(conn,uId,res,callback){
    conn = conn || getConnection();
    conn.query("SELECT * FROM order_rice WHERE uname = ? ", [uId], function(err, rows, fields) {
        if (err) {
            throw err;
            o = {code:1, msg:"系统发生非预期错误，请联系管理员"};
            res.end(JSON.stringify(o));
            return false;
            } else if (rows.length == 0) {
                row2 = null;
            } else {
                row2 = rows;
            }
            querycallback(row2);
    });
    function querycallback(row2){
        conn = conn || getConnection();
        conn.query("SELECT * FROM users WHERE uname = ? ", [uId], function(err, rows, fields) {
        if (err) {
            throw err;
            o = {code:1, msg:"系统发生非预期错误，请联系管理员"};
            res.end(JSON.stringify(o));

            return false;
            } else if (rows.length == 0) {
                row1 = null;
            } else {
                row1 = rows[0];
            }
            callback(row1,row2);
            conn.end();
            conn = null;
        });
    }
}
```
我实际上另外定义了一个回调函数，这样写避免了代码看起来太叠在一起。
这样再去执行，就可以完成查询了。

这是我对nodejs回调嵌套和异步的简单理解，欢迎读者反馈。