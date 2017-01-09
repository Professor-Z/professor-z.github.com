---
title: '[leetcode]344. Reverse String'
date: 2016-09-09 22:50:37
tags: leetcode
---
Write a function that takes a string as input and returns the string reversed.

#### Example:
Given s = "hello", return "olleh".

```JavaScript
/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
    var a = s.split("");
    a = a.reverse();
    a =  a.join("");
    return a;
};
```
