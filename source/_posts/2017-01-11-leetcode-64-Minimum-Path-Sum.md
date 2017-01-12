---
title: '[leetcode]64. Minimum Path Sum'
date: 2016-09-11 23:17:41
tags: leetcode 
---
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

```
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let m = grid.length,
        n=grid[0].length,
        sum = Array.from({length:m},(v,k)=>Array.from({length:n},(v,k)=>grid[0][0]));//空间可以优化
    for(let i=1;i<m;i++){
        sum[i][0] = sum[i-1][0] + grid[i][0];
    }
    for(let j=1;j<n;j++){
        sum[0][j] = sum[0][j-1] + grid[0][j];
    }
    for(let i=1;i<m;i++){
        for(let j=1;j<n;j++){
            sum[i][j] = Math.min(sum[i-1][j],sum[i][j-1]) + grid[i][j];
        }
    }
    return sum[m-1][n-1];
};
```

### 思路
这是一道典型的动态规划题目，每个点的最短路径取决于它左边和上面的点的最短路径，有公式`sum[i][j] = min(sum[i-1][j],sum[i][j-1]) + grid[i][j]`。
此公式非常简单，所以只需关注边界值，当点在边界上时，其最短路径等于其左边或上面的点的最短路径加其本身值。