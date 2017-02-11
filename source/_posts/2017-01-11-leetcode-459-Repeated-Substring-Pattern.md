---
title: '[leetcode]459. Repeated Substring Pattern'
date: 2016-09-11 22:58:44
tags: leetcode 
---
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

```
/**
 * @param {string} str
 * @return {boolean}
 */
var repeatedSubstringPattern = function(str) {
    // let compareString = (str1,str2)=>{
    //     for(let i=0;i<str1.length;i++){
    //         if(str1[i]!==str2[i]){
    //             return false;
    //         }
    //     }
    //     return true;
    // }
    let length = str.length;
    for(let i=2;i<=length;i++){
        if(length%i===0){
            let subLength = length/i,
                flag = true;
            let firstBase = str.slice(0,subLength);
            for(let j=1;j<i;j++){
                let seg = str.slice(subLength*j,subLength*(j+1));
                if(seg!==firstBase){
                    flag = false;
                    break;
                }
            }
            if(flag){
                return flag;
            }
        }
    }
    return false;
};
```

### 思路
把字符串均分，从2段~n(字符串长度)段依次尝试，对每次均分，如果出现每段都相等，则符合条件，如果直到均分为n段仍未成功，则不符合。

### 需注意
每次均分后的判断过程：出现不相等，则进行下次判断，直至最后每段均相等，则全局成功。
js slice 用法；