### LeetCode刷题笔记---1. Two Sum

[题目来源]: https://leetcode.com/problems/two-sum/

1. **题目描述：**

   ​	从给定的整型数组nums中找出和为给定数据target的两个数字，输出他们的下标（数组下标从0开始）。

   ​	注意：输入数组只有唯一输出解，且数组中的元素不重复出现。

2. **样例：**

   ```
   Given nums = [2, 7, 11, 15], target = 9,
   
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1].
   ```

3. **算法：**

   （一）C++

   ​	使用哈希表（算法时间复杂度：O（n））

   ​	循环一遍数组nums，在每一步循环的时候我们做两件事：

   ​		1.判断target-nums[i]是否在哈希表中；

   ​		2.将nums[i]添加到哈希表中；

   ​	时间复杂度：由于只扫描一遍，且哈希表的插入和查询操作的复杂度是O（1），所以总的时间复杂度是O（n）。

   ​	C++代码：

   ```c++
   #include <iostream>
   #include <vector>
   
   class Solution {
   public:
       vector<int> twoSum(vector<int>& nums, int target) 
       {
           vector<int> res;
           unordered_map<int,int> hash;
           for (int i = 0; i < nums.size(); i ++ )
           {
               int another = target - nums[i];
               if (hash.count(another))
               {
                   res = vector<int>({hash[another], i});
                   break;
               }
               hash[nums[i]] = i;
           }
           return res;         
       }
   };
   ```

   （二）python

   ​	在python里面有一个dictionary和C++的map功能一样。首先，我们建立一个字典，d = {},字典的key是数组的值num，value是相应的位置。只要满足num和 target - num 都是字典中的值，就输出这两个值的角标。

   ​	python代码：

   ```python
   class Solution:
       def twoSum(self, nums, target):
           dict = {}
           i = 0;
           for i in range(len(nums)):
               if dict.get(target - nums[i],None) == None:
                   dict[nums[i]] = i
               else:
                   return (dict[target-nums[i]],i)
           i = i+1
   ```
LeetCode刷题笔记---1. Two Sum
[题目来源]: https://leetcode.com/problems/two-sum/

1. **题目描述：**

   ​	从给定的整型数组nums中找出和为给定数据target的两个数字，输出他们的下标（数组下标从0开始）。

   ​	注意：输入数组只有唯一输出解，且数组中的元素不重复出现。

2. **样例：**

   ```
   Given nums = [2, 7, 11, 15], target = 9,
   
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1].
   ```

3. **算法：**

   （一）C++

   ​	使用哈希表（算法时间复杂度：O（n））

   ​	循环一遍数组nums，在每一步循环的时候我们做两件事：

   ​		1.判断target-nums[i]是否在哈希表中；

   ​		2.将nums[i]添加到哈希表中；

   ​	时间复杂度：由于只扫描一遍，且哈希表的插入和查询操作的复杂度是O（1），所以总的时间复杂度是O（n）。

   ​	C++代码：

   ```c++
   #include <iostream>
   #include <vector>
   
   class Solution {
   public:
       vector<int> twoSum(vector<int>& nums, int target) 
       {
           vector<int> res;
           unordered_map<int,int> hash;
           for (int i = 0; i < nums.size(); i ++ )
           {
               int another = target - nums[i];
               if (hash.count(another))
               {
                   res = vector<int>({hash[another], i});
                   break;
               }
               hash[nums[i]] = i;
           }
           return res;         
       }
   };
   ```

   （二）python

   ​	在python里面有一个dictionary和C++的map功能一样。首先，我们建立一个字典，d = {},字典的key是数组的值num，value是相应的位置。只要满足num和 target - num 都是字典中的值，就输出这两个值的角标。

   ​	python代码：

   ```python
   class Solution:
       def twoSum(self, nums, target):
           dict = {}
           i = 0;
           for i in range(len(nums)):
               if dict.get(target - nums[i],None) == None:
                   dict[nums[i]] = i
               else:
                   return (dict[target-nums[i]],i)
           i = i+1
   ```