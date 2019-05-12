**Task List**

数组->链表->栈->队列->递归->排序->二分查找->哈希表->字符串->二叉树->堆->图->回溯->分治->动态规划

### 01_array

1. 数组是**线性**数据结构,连续存放相同数据类型
2. 访问: 通过index访问 O(1), the index begins at 0.
3. 插入和删除: 中间插入，需要维护这个连续性，元素要重新放位置 O(n)，两头插入，O(1).

Three sum:  a + b + c = 0 ?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [] 
        for i in range(len(nums) - 2):
            j = i + 1 
            while j <= (len(nums) - 1):
                third = -(nums[i] + nums[j])
                if third in set(nums[j+1:]):
                    output.append([nums[i],nums[j],third])
                    j = j+1
                j = j + 1
        return output