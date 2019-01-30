### LeetCode刷题笔记（Week2）

#### 1. Two Sum

[题目来源]: https://leetcode.com/problems/two-sum/

1. ##### **题目描述：**

   ​	从给定的整型数组nums中找出和为给定数据target的两个数字，输出他们的下标（数组下标从0开始）。

   ​	注意：输入数组只有唯一输出解，且数组中的元素不重复出现。

2. ##### **样例：**

   ```
   Given nums = [2, 7, 11, 15], target = 9,
   
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1].
   ```

3. ##### **算法：**

   （一）C++

   ​	使用哈希表（算法时间复杂度：O（n））

   ​	循环一遍数组nums，在每一步循环的时候我们做两件事：

   ​		1.判断target-nums[i]是否在哈希表中；

   ​		2.将nums[i]添加到哈希表中；

   ​	时间复杂度：由于只扫描一遍，且哈希表的插入和查询操作的复杂度是O（1），所以总的时间复杂度是O（n）。

   ​	C++代码：见1. Two Sum.cpp

   （二）python

   ​	在python里面有一个dictionary和C++的map功能一样。首先，我们建立一个字典，d = {},字典的key是数组的值num，value是相应的位置。只要满足num和 target - num 都是字典中的值，就输出这两个值的角标。

   ​	python代码：见1. Two Sum.py

#### 2.Add Two Numbers

[题目来源]: https://leetcode.com/problems/add-two-numbers/

1. ##### **题目描述：**

   ​	给定两个非空链表S1、S2，各代表一个非负整数，顺序从低位（个位）到高位，请计算两个整数的和，并返回成链表形式。

   ​	注意：数据中两个整数的开头都不为0（除了整数0本身）。

2. **样例：**

   ```
   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
   Output: 7 -> 0 -> 8
   Explanation: 342 + 465 = 807.
   ```

3. **算法：**

   （一）C++

   ​	这是一道模拟加法题。

   ​	加法规则：低位满10向高位进1；如果最高位有进位，则需在最前面补1.

   ​	C++代码：见2.Add Two Numbers.cpp

   （二）python

   ​	题目意在模拟加法运算，只需要从低位（链表第一位）开始，同位相加，满10往高位（链表下一位）进1。

   ​	python代码：见2.Add Two Numbers.py

#### 3、 Longest Substring Without Repeating Characters

[题目来源]: https://leetcode.com/problems/longest-substring-without-repeating-characters/

1. ##### **题目描述：**

   ​	从给定的字符串s中找到其不含重复字母的最长子串，输出其长度。

   ​	注意：找最长子串(连续的而一段)，而不是子序列（不一定是连续的一段）。

2. ##### **样例：**

   ```
   Example 1:
   Input: "abcabcbb"
   Output: 3 
   Explanation: The answer is "abc", with the length of 3.
   
   Example 2:
   Input: "bbbbb"
   Output: 1
   Explanation: The answer is "b", with the length of 1.
   
   Example 3:
   Input: "pwwkew"
   Output: 3
   Explanation: The answer is "wke", with the length of 3. 
                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
   ```

3. **算法：**

   python

   ​	从字符串开头往后找，发现有重复字母出现时，重新以当前的重复字母开始往后找，不断按上述步骤进行，直到找到满足题目要求的最长子串，输出其长度。

   ​	python代码：见3.Longest Substring Without Repeating Characters.py

### 7.Reverse Integer

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

   ​	C++代码：见7.Reverse Integer.cpp

   （二）python

   ​	将整型数的符号位单独提取出来，这样就只需要考虑数值位反转，我们用strx = str(abs(x))来将整型数返回成一个string格式的字符串，然后用”r = strx[::-1]“语句倒序输出。最后，将符号位相乘即可。

   ​	python代码：见7.Reverse Integer.py

### 8.String to Integer (atoi)

[题目来源]: https://leetcode.com/problems/string-to-integer-atoi/

1. **题目描述：**

   ​	atoi* (表示 ascii to integer)是把字符串转换成整型数的一个函数；此题应用该函数完成字符串到数值的转换。若给定字符串开头为空格，继续向后读取直到开头不为空为止；从这个数据开始读取，允许数值前面带有正负（+、-）号，然后把所有数值转换成一个整型数。允许字符串中数值部分之后有其他字符，处理过程中忽略其存在即可。

   ​	注意：

   ​		若原数据为空或者不是以数字（包括正负号）开头，则不进行				转换，输出0。

   ​		假设我们用32位整型，其数据范围为 [−2<sup>31</sup>,  2<sup>31</sup>− 1]，若超出数据表示范围，则输出同符号的边界值。

2. **样例：**

   ```
   Example 1:
   Input: "42"
   Output: 42
   
   Example 2:
   Input: "   -42"
   Output: -42
   Explanation: The first non-whitespace character is '-', which is the minus sign.
         Then take as many numerical digits as possible, which gets 42.
   
   Example 3:
   Input: "4193 with words"
   Output: 4193
   Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
   
   Example 4:
   Input: "words and 987"
   Output: 0
   Explanation: The first non-whitespace character is 'w', which is not a numerical 
                digit or a +/- sign. Therefore no valid conversion could be performed.
   
   Example 5:
   Input: "-91283472332"
   Output: -2147483648
   Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                Thefore INT_MIN (−231) is returned.
   ```

3. **算法：**

   python

   ​	将输入字符串中的符合条件的整型数提取出来，只考虑数值部分。

   ​	python代码：见8.String to Integer (atoi).py

### 9.Palindrome Number

[题目来源]: https://leetcode.com/problems/palindrome-number/

1. **题目描述：**

   ​	判断一个整型数是否为palindrome（若整数反转之后仍为原数，则是；反之不是）。

   ​	注意：若数据为负，则一定不是。

2. **样例：**

   ```
   Example 1:
   Input: 121
   Output: true
   
   Example 2:
   Input: -121
   Output: false
   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
   
   Example 3:
   Input: 10
   Output: false
   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
   ```

3. **算法：**

   python

   ​	将输入数据转换成一个字符串，然后逆序看是否一致。

   ​	python代码：见9.Palindrome Number.py