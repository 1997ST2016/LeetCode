### LeetCode刷题笔记（Week2）

[题目来源]: https://leetcode.com/problemset/all/

#### 11.Container With Most Water				

**题目描述：**

​	给定n个非负整数a<sub>1</sub>,a<sub>2</sub>,...a<sub>n</sub>,每个数代表一个坐标（i，a<sub>i</sub>），画出n条垂直的线段。a<sub>i</sub>，a<sub>j</sub>为高，i到j为底，可以构造出一个容器。从其中找出两条，使得两者围成的容器容积最大,输出可装水的最大容量。

​	注意：容器不能倾斜且n>2。

**案例：**

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

如下图所示：

![](D:\MyUniversity\Leetcode\Week2\11. Container With Most Water.png)

**题目思路：**

​	考虑短板效应（水容积的大小由短高度决定）。

​	尺取法：通常是指对数组保存一对下标，即取区间的左右端点，然后根据实际情况不断地推进去见左右端点以得出答案使用尺取法时应清楚以下四点：
​	(1)什么情况下能使用尺取法?  

​	(2)何时推进区间的端点？ 

​	(3)如何推进区间的端点？

​	(4)何时结束区间的枚举？

​	在本道题中，我们用两个指针i,j分别指向首尾，如果a<sub>i</sub>>a<sub>j</sub>,则j--；否则i++,直到i=j为止，每次迭代更新最大值。

​	C++代码：暴力解法：见11.Container With Most Water.cpp

​			双指针法：见11.Container With Most Water(DoublePointer).cpp

​	python代码：见11.Container With Most Water.py

#### 12.Integer to Roman 

**题目描述：**

​	想给定整型数转换为罗马数字。罗马数字用七个不同的符号表示：I,V,X,L,C,D和M，它们的含义如下：

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

​	注意：数据范围：1~3999.

**案例：**

```
Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**题目思路：**

​	需要知道罗马数字和整型数的转换规则，注意特殊数值的表示：900，500，400，90，50，40，9，5，4分别对应的是‘CM’，‘D’，‘CD’，‘XC’，‘L’，‘XL’，‘IX’，‘V’，‘IV’。

​	python代码：见12.Integer to Roman.py  

#### 13.Roman to Integer

**题目描述：**

​	罗马数字转换成整型数据，对应规则见上道题。

​	注意：数据表示范围：1~3999

**案例：**

```
Example 1:
Input:  "III"
Output: 3

Example 2:
Input:  "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**题目思路：**

​	python代码：见13.Roman to Integer.py 

#### 14.Longest Common Prefix

**题目描述：**

​	找出给定字符串组strx中的最长公共前缀子字符串。

​	注意：如果没有共同前缀，返回空字符串。

**案例：**

```
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**题目思路：**

​	初始化公共前缀子字符串strs[0]，从字符串头部开始计算，比较每个字符串中的字符，得到公共前缀子字符串，直到比较到字符串的最后一个字符。

​	python代码：见14.Longest Common Prefix.py

#### 15.3Sum 

**题目描述：**

​	给定一个含有n个整型数字的数组nums，判断nums中是否含有三个元素使其和为0，给出所有可能的组合。

​	注意：一组三个数中不包含重复数字。

**案例：**

```
Example ：
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

**题目思路：**

​	首先将数组中的元素排序，然后从头开始读取数据num[i]，在该数据之后的剩余元素中找num[j],num[k]使得他们的和为0-num[i]，剩余做法参考题目1。

​	python代码：见15.3Sum .py

#### 17.Letter Combinations of a Phone Number

**题目描述：**

​	给定一个包含数字2-9的字符串，输出数字所能表示的所有字母组合。

字母键盘如下图：

![](D:\MyUniversity\Leetcode\Week2\17.Letter Combinations of a Phone Number.png)

​	注意：数字1不匹配任何字母；字母顺序任意。

**案例：**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**题目思路：**

​	用向量的笛卡尔乘积，笛卡尔乘积是指在数学中，两个集合*X*和*Y*的笛卡尓积（Cartesian product），又称直积，表示为*X* × *Y*，第一个对象是*X*的成员而第二个对象是*Y*的所有可能有序对的其中一个成员。首先建立一个字典：dict ={'0':'','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}；然后利用笛卡尔乘积得到答案。

​	python代码：见17.Letter Combinations of a Phone Number.py 
