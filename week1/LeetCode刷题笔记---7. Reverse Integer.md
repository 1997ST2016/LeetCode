### LeetCode刷题笔记---7. Reverse Integer

[题目来源]: https://leetcode.com/problems/reverse-integer/

1. **题目描述：**

   ​	将给定的32位带符号整型数x进行数值位反转，如果反转之后的数据溢出，则返回0。

   ​	注意：若原数据x为负数，反转后仍为负数；

   ​		若原数据x的最后一位为0，反转后数据位数减少一位。

   ​	补充：32位带符号整型数的表示范围： [−2<sup>31</sup>,  2<sup>31</sup>− 1]

2. **样例：**

   ```
   Example 1:
   Input: 123
   Output: 321
   
   Example 2:
   Input: -123
   Output: -321
   
   Example 3:
   Input: 120
   Output: 21
   ```

3. **算法：**

   （一）C++

   ​	将数字从右向左计算出每位数字，然后逆序按权相加在一个整型数中。由于反转后的数据可能溢出，所以设中间变量tem为long long 型。

   ​	C++代码：

   ```c++
   class Solution {
   public:
       int reverse(int x) {
           long long tem = 0;
           while(x)
           {
               tem = tem * 10 + x % 10;
               x /= 10;
           }
               if (tem < -2147483648|| tem > 2147483647) return 0;
               return tem;    
       }
   };
   ```

   （二）python

   ​	将整型数的符号位单独提取出来，这样就只需要考虑数值位反转，我们用strx = str(abs(x))来将整型数返回成一个string格式的字符串，然后用”r = strx[::-1]“语句倒序输出。最后，将符号位相乘即可。

   ​	python代码：

   ```python
   import math
   class Solution(object):
       def reverse(self, x):
           """
           :type x: int
           :rtype: int
           """
           if x<0:
               sign = -1
           else:
               sign = 1
           strx = str(abs(x))
           r = strx[::-1] 
           if int(r)>2**31:
               return 0
           else:
               return sign*int(r)
   ```
