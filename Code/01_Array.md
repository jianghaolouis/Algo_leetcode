## 01_array

1. 数组是**线性**数据结构,连续存放相同数据类型
2. 访问: 通过index访问 O(1), the index begins at 0.
3. 插入和删除: 中间插入，需要维护这个连续性，元素要重新放位置 O(n)，两头插入，O(1).

### 15 Three sum:  a + b + c = 0 ?

[-1, 0 , 1 , 2 , -1 , -4] -> [[-1,1,0], [-1,-1,2]]

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]: continue
            j = i + 1
            k = len(nums) - 1
            while j < k: 
                sum_3 = nums[i] + nums[j] + nums[k]
                if sum_3 == 0:
                    Res.append([nums[i],nums[j],nums[k]])
                    while j<(len(nums)-2) and nums[j]==nums[j+1]:
                        j+=1
                    while k>j and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif sum_3 > 0:
                    k-=1
                else:
                    j+=1 
        return Res
```



### 169 Majority element

find the element that the frequency  > [n/2] times

-  Method 1 : Hash maps {value, time} 

   ```python
   class Solution:
       def majorityElement(self, nums):
           counts = collections.Counter(nums)
           return max(counts.keys(), key = counts.get)    
   ```

   collections 是python 内置的container， dict.keys 返回所有的key,  第二个key是max的内置排序func选择， .get是得到字典的value, 所以是按照value取最大值然后输出对应的key

   

-  Method 2 : Sort  排完序后的中间元素一定是超过一般元素个数的。 

   ```python
   class Solution:
       def majorityElement(self, nums):
           nums.sort()
           return nums[int(len(nums)/2)]
   ```

-  Method 3 : Boyer-Moore Voting Algorithm

   count 不同的元素相互抵消 -1，相同的元素组团 +1，最后留下的元素一定是众数。

   ```python
    def majorityElement(self, nums):
           count = 0
           Candidate = None
           for num in nums:
               if count == 0:
                   candidate = num
               count += (1 if num == candidate else -1)
          	return candidate
   ```

   

### 41 First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer. Your algorithm should run in **O*(*n*)*** time and uses constant extra space.

[3,4,-1,1] -> 2

分析: 我们先到一个最小的正数，是min = 1，然后最大值可以达到 max= nums.length. 如果排一个序的话，应该是 1, 3, 4 其实中间的一个数原本是丢失的2，但是被-1给取代了。所以我们应该把每一个数放回它应该在的位置： 1 在 index 0， 3在index 2, 4在index 3。 可以用hash去模仿这个过程。

Hash func : f = nums[i] - 1

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # nums[nums[i] - 1] != nums[i] 检查元素nums[i]的slot是否在它应该的位置上
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                #应该把这个元素i换到它自己的位置上，然后把原来占位的元素给换出来
                x  = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = x
        # 找出那个missing number
        for i in range(len(nums)):
            if (nums[i] != i + 1) : return (i + 1)
        return len(nums) + 1
```

这里的**while**非常重要，不能用if代替，因为i位置的元素换到它应该的位置后，被还回来的那个元素一般也不应该在 i 位置，所以要继续在 i 位置进行置换操作。