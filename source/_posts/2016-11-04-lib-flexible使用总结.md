---
title: "lib-flexible 使用总结"
tags: CSS
date: 2016-11-04 21:50:04
---

`lib-flexible` 是淘宝前端团队开源的一种用于移动端跨屏适配的『可伸缩布局方案』。主要部分（另一部分是栅格方案，此处不表）代码总共117行，原理也非常简单（本文后附源码注释）。

## 解决的问题
`lib-flexible`主要解决了开发者的两大痛点。第一是移动端设备的视口宽度（也即 window.innerWidt 也即viewport*initial-scale）各不相同，如果按照电脑端的开发风格（使用 px）来设置页面元素尺寸，会使得不同设备上布局风格差别很大。理想的方式是按照固定比例设置元素尺寸，但如果使用百分比，由于 CSS 的相关规则，实现起来会比较复杂。

rem 的出现对解决这个问题提供了很大的帮助。rem 含义是页面根元素（也即 html 标签）上设置的 font-size 值，在整个页面范围内，rem 的值是不变的。这样，我们便可以这样解决元素尺寸跨屏适配问题：
```
1.将 rem 单位与设备视口宽度挂钩。比如，lib-flexible 中设置的 1 rem 便是视口宽度的 1/10。

2.将设计稿中元素尺寸与视口宽度的关系反映到 px 单位与 rem 单位的换算中去。 
```
这样多设备适配的问题便有了很好的解决方案。

`lib-flexible` 解决的第二个问题是 retina 屏幕设备显示效果问题。如果按照设备本来的视口宽度实现元素尺寸，会导致设备像素比（dpr:window.devicePixelRatio）较高的屏幕上出现 1 px border 问题，同时图片也会看起来不够清晰。这都是由于高 dpr 设备中 CSS 的 1px 宽度代表了设备上的 dpr 宽度。如果能够使得 CSS 的 1px 确实能表示设备上的1小格，上述问题便能迎刃而解。

`lib-flexible` 通过设置 meta 元素中的 viewport 值中的 initial-scale 字段对页面进行缩放(innerWidth = device-width/initial-scale)，将设备 dpr 改为了1。解决了上述问题。

## 缺点
虽然lib-flexible 解决了上述问题，但也带来了一些其它的问题。

1.与其他代码兼容

由于引入了高清屏适配，因而所有本页面内的 html 元素的尺寸都必须使用 rem 为单位才能达到跨屏适配的效果，这就使得兼容没有使用高清屏幕适配的代码成为了问题。而解决这个问题只有两个办法。
```
1.在 meta 中设置 initial-sale=1 禁用掉高清屏缩放，这样便能直接使用以 px 为单位的代码，这样最为简单，但同时那些 以px 为单位布局的元素还是会有多屏尺寸不一致的问题微信开源的 weui.css 便是一个例子。

2.不修改 initial-scale ，重写之前的代码，也应用 rem 方案，只是这样会增加一定的工作成本。
```

## 源码注释
```javascript
;(function(win, lib) {
    var doc = win.document;
    var docEl = doc.documentElement;
    var metaEl = doc.querySelector('meta[name="viewport"]');
    var flexibleEl = doc.querySelector('meta[name="flexible"]');
    var dpr = 0;//设备像素比，与缩放比例程倒数关系
    var scale = 0;//缩放比例
    var tid;
    var flexible = lib.flexible || (lib.flexible = {});
    //通过已有的 viewport 或 flexible 标签设置 scale 和 dpr。
    // 优先级为：1,viewport 2，flexible 标签中的 initial-dpr 值 3，flexible 标签中的 maximum-dpr 值
    if (metaEl) {
        console.warn('将根据已有的meta标签来设置缩放比例');
        var match = metaEl.getAttribute('content').match(/initial\-scale=([\d\.]+)/);
        if (match) {
            scale = parseFloat(match[1]);
            dpr = parseInt(1 / scale);
        }
    } else if (flexibleEl) {//不太懂这里有什么用，后面也没有设置 flexible ,猜测可能是淘宝团队之前约定使用此标签处理相关问题
        var content = flexibleEl.getAttribute('content');
        if (content) {
            var initialDpr = content.match(/initial\-dpr=([\d\.]+)/);
            var maximumDpr = content.match(/maximum\-dpr=([\d\.]+)/);
            if (initialDpr) {
                dpr = parseFloat(initialDpr[1]);
                scale = parseFloat((1 / dpr).toFixed(2));    
            }
            if (maximumDpr) {
                dpr = parseFloat(maximumDpr[1]);
                scale = parseFloat((1 / dpr).toFixed(2));    
            }
        }
    }
    //如果没有设置 viewport 和 flexible 标签值
    if (!dpr && !scale) {
        var isAndroid = win.navigator.appVersion.match(/android/gi);
        var isIPhone = win.navigator.appVersion.match(/iphone/gi);
        var devicePixelRatio = win.devicePixelRatio;
        if (isIPhone) {
            // iOS下，根据window.devicePixelRatio 来设置 dpr 值
            if (devicePixelRatio >= 3 && (!dpr || dpr >= 3)) {                
                dpr = 3;
            } else if (devicePixelRatio >= 2 && (!dpr || dpr >= 2)){
                dpr = 2;
            } else {
                dpr = 1;
            }
        } else {
            //安卓设备设置 dpr = 1
            dpr = 1;
        }
        scale = 1 / dpr;
    }
    //设置 data-dpr 值
    docEl.setAttribute('data-dpr', dpr);
    // 如果没有 viewport 值，设置 scale 值，并禁止缩放，添加 viewport 信息到head、
    if (!metaEl) {
        metaEl = doc.createElement('meta');
        metaEl.setAttribute('name', 'viewport');
        metaEl.setAttribute('content', 'initial-scale=' + scale + ', maximum-scale=' + scale + ', minimum-scale=' + scale + ', user-scalable=no');
        if (docEl.firstElementChild) {
            docEl.firstElementChild.appendChild(metaEl);
        } else {
            var wrap = doc.createElement('div');
            wrap.appendChild(metaEl);
            doc.write(wrap.innerHTML);
        }
    }
    // 设置 rem 值为设备宽度 1/10，如果页面宽度/dpr 超过 540 则按照 540
    function refreshRem(){
        var width = docEl.getBoundingClientRect().width;
        if (width / dpr > 540) {
            width = 540 * dpr;
        }
        var rem = width / 10;
        docEl.style.fontSize = rem + 'px';
        flexible.rem = win.rem = rem;
    }
    //在 resize 和 pageshow 事件 300ms 后重新设置 rem 值
    win.addEventListener('resize', function() {
        clearTimeout(tid);
        tid = setTimeout(refreshRem, 300);
    }, false);
    win.addEventListener('pageshow', function(e) {
        if (e.persisted) {
            clearTimeout(tid);
            tid = setTimeout(refreshRem, 300);
        }
    }, false);
    //文档加载完成之后 设置 body 标签的 font-size ，消除rem 对字体的影响
    if (doc.readyState === 'complete') {
        doc.body.style.fontSize = 12 * dpr + 'px';
    } else {
        doc.addEventListener('DOMContentLoaded', function(e) {
            doc.body.style.fontSize = 12 * dpr + 'px';
        }, false);
    }
    

    refreshRem();
    //在 lib.flexible 上注册一些属性值和方法
    flexible.dpr = win.dpr = dpr;
    flexible.refreshRem = refreshRem;
    flexible.rem2px = function(d) {
        var val = parseFloat(d) * this.rem;
        if (typeof d === 'string' && d.match(/rem$/)) {
            val += 'px';
        }
        return val;
    }
    flexible.px2rem = function(d) {
        var val = parseFloat(d) / this.rem;
        if (typeof d === 'string' && d.match(/px$/)) {
            val += 'rem';
        }
        return val;
    }

})(window, window['lib'] || (window['lib'] = {}));

```