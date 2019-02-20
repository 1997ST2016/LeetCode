### LeetCode刷题笔记（Week3）

[题目来源]: https://leetcode.com/problemset/all/

#### 24. Swap Nodes in Pairs

**题目描述：**

​	给定一个链表，每两个相邻节点的值进行交换。

​	注意：不改变结点的值；不能建立新链表。

**案例：**

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

**题目思路：**

首先建立一个头结点，将头结点指向第二个结点，再指向第一	个结点，然后再指向第四个结点点，最后第三个结点，后续跳过第二个节点继续重复之前的操作。

​	C++代码：见24. Swap Nodes in Pairs.cpp

​	python代码：见24. Swap Nodes in Pairs.py

#### 26. Remove Duplicates from Sorted Array 

**题目描述：**

​	给定一个排好序的数组，其中重复的元素只保留一个，去除多余的，返回新数组的长度。

​	注意：不能申请额外数组的空间，只能用常数的空间来实现。

**案例：**

```
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

**题目思路：**

​	给定的的数组已经有序，那么我们用i,j两个下标，i记录新数组的下标，j为原数组的下标。比较当前元素与前一个元素是否一致，相同则跳过，否则将当前元素加入新数组。

​	python代码：见26. Remove Duplicates from Sorted Array.py

数组  OR  数

#### 27. Remove Element

**题目描述：**

​	给定一个数组nums和值val，将数组中等于val的数去除。

​	注意：不能申请额外的空间。

**案例：**

```
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
```

**题目思路：**

​	和上一道题一样，有i,j两个下标变量，如果nums[j] ！= val，那么nums[i] = nums[j]，i、j各加1。

​	python代码：见27. Remove Element.py

#### 28. Implement strStr()

**题目描述：**

​	返回字符串needle在字符串haystack中第一次出现的索引，如果needle不是haystack字符串的子串时输出-1。

​	注意：当字符串needle的长度为0时，输出0。

**案例：**

```
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**题目思路：**

​	先考虑特殊情况：当字符串needle为空时返回0，当needle长度大于haystack时返回-1。然后考虑一般情况：从i=0出发，如果遇到haystack[i] == needle[0]，那么判断从这个出发能不能构成needle，如果可以则返回i。直到i到最后一个字符的长度小于needle的长度。

​	python代码：见28. Implement strStr().py



#### 29. Divide Two Integers

**题目描述：**

​	给定两个整型数，分别为被除数（dividend）和除数（divisor），返回被除数除以除数所得的商（quotient）。

​	注意：被除数和除数均为32位整型数；

​		除数不为0；

​		不使用乘法、除法和取余操作。

**案例：**

```
Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
```

**题目思路：**

​	python代码：见29. Divide Two Integers.py