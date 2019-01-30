​					LeetCode刷题笔记---第二周

[题目来源]: https://leetcode.com/problemset/all/

11. Container With Most Water	（Medium）				

**题目描述：**

​	给定n个非负整数a<sub>1</sub>,a<sub>2</sub>,...a<sub>n</sub>,每个数代表一个坐标（i，a<sub>i</sub>），画出n条垂直的线段。a<sub>i</sub>，a<sub>j</sub>为高，i到j为底，可以构造出一个容器。从其中找出两条，使得两者围成的容器容积最大,输出可装水的最大容量。

​	注意

**案例：**

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

如下图所示：

![](D:\My University\Leetcode\Week2\11. Container With Most Water.png)

**题目思路：**

​	考虑短板效应（水容积的大小由短高度决定）。

​	python代码：

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)   
        maxv = 0 
        j = 0
        k = size - 1
        while j < k:
            if height[j] <= height[k]:
                maxv = max(maxv,height[j] * (k - j))
                j += 1
            else:
                maxv = max(maxv,height[k] * (k - j))
                k -= 1
        return maxv
```

12. Integer to Roman 

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

    ​	python代码：

    ```python
    class Solution(object):
        def intToRoman(self, nums):
            """
            :type num: int
            :rtype: str
            """
            a = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
            b = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
            ans = ''
            i = 0
            count = 0
            while nums > 0:
                count = nums/a[i]
                nums %= a[i]
                while count > 0:
                    ans += b[i]
                    count -= 1
                i += 1
            return ans
    ```

13. Roman to Integer

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

    ​	python代码：

    ```python
    class Solution(object):
        def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  
            sum = 0 
            size = len(s)   
            i = 0     
            while i < size:     
                if i > 0 and d[s[i]] > d[s[i-1]]:         
                    sum += d[s[i]] -2*d[s[i-1]]   
                else:         
                    sum += d[s[i]]         
                i += 1
            return sum
    ```

14. Longest Common Prefix

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

    ​	python代码：

    ```python
    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            size = len(strs)
            if size == 0:
                return ''
            if size == 1:
                return strs[0]
            ans = strs[0]
            i = 1
            for i in range (size):
                j = 0
                minlen = min(len(ans),len(strs[i]))
                while j < minlen:
                    if ans[j] != strs[i][j]:
                        break
                    j +=1
                if j == 0:
                    return ''
                ans = ans[: j]
                i += 1
            return ans
    ```

15.  3Sum 

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

    ​	python代码：

    ```python
    class Solution(object):
        def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            size = len(nums)
            ans = []
            if size <= 2:
                return ans
            nums.sort()
            i = 0
            while i < size -2:
                tmp = 0 - nums[i]
                j = i + 1
                k = size -1
                while j < k:
                    if nums[j] + nums[k] < tmp:
                        j += 1
                    elif nums[j] + nums[k] > tmp:
                        k -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while j < k:
                            if nums[j] != nums[j - 1]:
                                break
                            if nums[k] != nums[k + 1]:
                                break
                            j += 1
                            k -= 1
                i += 1
                while i < size - 2:
                    if nums[i] != nums[i - 1]:
                        break
                    i += 1
            return ans
    ```

    17.Letter Combinations of a Phone Number

    **题目描述：**

    ​	给定一个包含数字2-9的字符串，输出数字所能表示的所有字母组合。

    字母键盘如下图：

    ![](D:\My University\Leetcode\Week2\17.Letter Combinations of a Phone Number.png)

    ​	注意：数字1不匹配任何字母；字母顺序任意。

    **案例：**

    ```
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    ```

    **题目思路：**

    ​	用向量的笛卡尔乘积，笛卡尔乘积是指在数学中，两个集合*X*和*Y*的笛卡尓积（Cartesian product），又称直积，表示为*X* × *Y*，第一个对象是*X*的成员而第二个对象是*Y*的所有可能有序对的其中一个成员。首先建立一个字典：dict ={'0':'','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}；然后利用笛卡尔乘积得到答案。

    ​	python代码：

    ```python
    class Solution(object):
        def addDigit(self,digit,ans):
            tmp = []
            for element in digit:
                if len(ans) == 0:
                    tmp.append(element)
                for s in ans:
                    tmp.append(s + element)
            return tmp
        def letterCombinations(self, digits):
            """
            :type digits: str
            :rtype: List[str]
            """
            ans = []
            d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            for element in digits:
                ans = self.addDigit(d[element],ans)
            return ans
    ```