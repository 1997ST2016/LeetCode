### LeetCode刷题笔记（Week3）

[题目来源]: https://leetcode.com/problemset/all/

#### 43. Multiply Strings

**题目描述：**

​	给定两个以字符串形式表示的非负整数num1和num2，将两个数字相乘，并以字符串形式返回乘积。

​	注意：两个数字均小于110；

​		两个数字只包含数字0-9；

​		两个数字均不以‘0’开头，除了数字0本身；

​		不能直接采用内置的BigInteger库或者转换整型数的输入。

**案例：**

```
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**题目思路：**

先反序，再统计位数，取模是本位上的数，除以10是进位的数。

​	python代码：见43. Multiply Strings.py

#### 46. Permutations

**题目描述：**

​	给定一组不同的整型数，返回所有可能的排列。

**案例：**

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

**题目思路：**

​	递归思想，用dfs分析所有可能性。

​	python代码：见46. Permutations.py

#### 47. Permutations II

**题目描述：**

​	给定一组可能包含相同数字的整型数，返回所有可能的不同排列。

**案例：**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

**题目思路：**

​	和上一道题相似，区别在本题中给定的一组数可以包含重复数字。设置一个标志flag来记录数字是否出现过。

​	python代码：见47. Permutations II.py

#### 48. Rotate Image

**题目描述：**

​	给定一个n×n的矩阵matrix，其代表一张图，将该图片顺时针旋转90°并输出；即矩阵的转置。

​	注意：图片需在原地旋转，不能单独开辟存储空间。

**案例：**

```
Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

**题目思路：**

​	行列互换，等同于转置。

​	python代码：见48. Rotate Image.py

#### 53. Maximum Subarray

**题目描述：**

​	给定一个整型数组nums，找到连续子串（至少包含一个数字）使其和最大，输出他们的和。

​	注意：图片需在原地旋转，不能单独开辟存储空间。

**案例：**

```
Example 1:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**题目思路：**

​	用动态规划的思想：b[j] = max{b[j - 1] + a[j],a[j]}

​	python代码：见53. Maximum Subarray.py

#### 54. Spiral Matrix

​	给定一个m×n的矩阵matrix（m行n列），以螺旋序输出所有元素。

**案例：**

```
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**题目思路：**

​	