### LeetCode刷题笔记（Week3）

[题目来源]: https://leetcode.com/problemset/all/

#### 33. Substring with Concatenation of All Words

**题目描述：**

给定一个翻转之后的数组nums，输出给定的数值target在数组中的位置；如果nums中不包含target值，输出-1。

翻转数组：指将原来升序排列的数组以某一点为中心，将这一点之前的元素放在此点之后所得的数组。如`[0,1,2,4,5,6,7]` 可以翻转成 `[4,5,6,7,0,1,2]`)。

要求：假设数组中不包含重复数值；

​	算法的时间复杂度为*O*(log *n*)。

**案例：**

```
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**题目思路：**

折半查找

​	python代码：见33. Search in Rotated Sorted Array.py

#### 34. Find First and Last Position of Element in Sorted Array

**题目描述：**

​	给定一个升序排列的整型数组，找到值为target的第一个和最后一个元素，并输出它们的下标；如果nums中不包含target值，输出[-1,-1]。

​	要求：算法的时间复杂度为*O*(log *n*)。

**案例：**

```
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**题目思路：**

​	给定的的数组已经有序，那么我们用i,j两个下标，i从前往后遍历数组，记录下标，j从后往前，比较元素的值，保存target的下标。

​	python代码：见34. Find First and Last Position of Element in Sorted Array.py

#### 35. Search Insert Position

**题目描述：**

​	给定一个有序数组nums和值target，如果target值可以在元素中找到，返回target值的下标；若找不到，返回该元素插入数组的位置。

​	注意：数组中没有重复元素。

**案例：**

```
Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
```

**题目思路：**

​	折半查找。

​	python代码：见35. Search Insert Position.py

#### 38. Count and Say

**题目描述：**

​	Count-and-Say序列的规则：某个字符连续出现的次数+该字符；比如“11”就是2个1，也就是得到“21”；初始字符串为“1”。

前五个序列如下：

```
1.     1       	1 is read off as "one 1" or 11.
2.     11		11 is read off as "two 1s" or 21.
3.     21		21 is read off as "one 2, then one 1" or 1211.
4.     1211
5.     111221
```

​	输入一个正数n（1 ≤ *n* ≤ 30），生成满足上述规则的第n个序列。

注意：每个序列的术语表示为一个字符串。

**案例：**

```
Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
```

**题目思路：**

​	python代码：见38. Count and Say.py



#### 39. Combination Sum

**题目描述：**

​	给定一组无重复的候选数字candidates和目标值target，在candidates中找到所有不同组合使得其和为target。

注意：所有的数字均为正整数；

​	解集中不包含重复组合。

**案例：**

```
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

**题目思路：**

​	写出dfs函数，将目标值target不断划分为更小的数，递归调用dfs函数，直到找到所有满足条件的组合。

​	python代码：见39. Combination Sum.py

#### 40.  Combination Sum II

**题目描述：**

​	给定一组候选数字candidates和目标值target，在candidates中找到所有不同组合使得其和为target。

注意：数字candidates中的每个值只能用一次；

​	所有的数字均为正整数；

​	解集中不包含重复组合。

此题与上一题的区别为：

​	给定数组中包含重复数字；

​	组合要求candidates中每个元素只能用一次；

**案例：**

```
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

**题目思路：**

​	遇上一题思路类似，此题多加一个flaglist，用来标记数字是否用过；若用过，标记取值为1，否则为0。

​	python代码：见40. Combination Sum II.py

