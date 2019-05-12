**Task List**

数组->链表->栈->队列->递归->排序->二分查找->哈希表->字符串->二叉树->堆->图->回溯->分治->动态规划

##  01_array

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

   ````python
   class Solution:
       def majorityElement(self, nums):
           counts = collections.Counter(nums)
           return max(counts.keys(), key = counts.get)    
   ````

   collections 是python 内置的container， dict.keys 返回所有的key,  第二个key是max的内置排序func选择， .get是得到字典的value, 所以是按照value取最大值然后输出对应的key

   

-  Method 2 : Sort  排完序后的中间元素一定是超过一般元素个数的。 

   ````python
   class Solution:
       def majorityElement(self, nums):
           nums.sort()
           return nums[int(len(nums)/2)]
   ````

-  Method 3 : Boyer-Moore Voting Algorithm

   count 不同的元素相互抵消 -1，相同的元素组团 +1，最后留下的元素一定是众数。

   ````python
    def majorityElement(self, nums):
           count = 0
           Candidate = None
           for num in nums:
               if count == 0:
                   candidate = num
               count += (1 if num == candidate else -1)
          	return candidate
   ````

   

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

## 02_LinkedList

1. 数组将元素顺序存储在内存单元里，静态分配。 链表是通过元素的指针，将元素存储在零散的内存中，动态内存分配。
2. 插入，删除时，链表直接修改前后元素的指针，O(1)。 而查找一个元素的时候，需要从第一个元素开始遍历。O(n)
3. 链表构建head元素的指针，其他的都通过head查找。

Question: 

1. 实现单链表、循环链表、双向链表，支持增删操作
2. 实现单链表反转
3. 实现两个有序的链表合并为一个有序链表
4. 实现求链表的中间结点



### 206 Reverse single linked-list

Input : 1->2->3->4->None

Output: 4->3->2->1->None

分析:

1. 首先链表的输入是一个head头指针
2. 基本方法是让当前的节点指向prev的一个节点，但是要先把当前节点原来指向的节点保存下来 storePtr = cur.next
3. 让当前的节点指针指向前一个元素 cur.next = prev
4. 完成节点指针调转后，把prev和cur都向前移一步: prev = cur;  cur = storePtr
5. 不断的循环 cur 的节点，直到它指向None说明已经到了原链表的尾，此时的prev正好是新链表的head


```python
# 定义一个节点 Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 一个链表只保存了它的head表头地址
# 非循环方法
def non_recur_reverse(head):
    if head is None or head.next is None:
        return head
    
    pre = None
    cur = head
    while cur :
        storePtr = cur.next
        cur.next = pre
        pre = cur
        cur = storePtr
    return pre

# 循环方法
def recurse(head):
    if head is None:
        return ;
    if head.next is None:
        return newhead = head
    else:
        newhead = recurse(head.next)
        head.next.next = head
        head.next = None
    return newhead

if __name__ == "__main__":
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3
    p = reverse(head)
    while p: 
        print(p.val)
        p = p.next
    
    Output: 4 3 2 1
```

### 21 Merge two linked list

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

分析:

1. 首先这是两个排序好的链表。一般是分别比较两个列表的当前元素大小L1[i] 和 L2[j], 然后取较小， 再increment.
2. 一旦发现有那个链表的元素都比较完了，指向了None，那么可以直接把剩下的非空的链表全部加到合并的链表后面。

```python
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

```python
# define a Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if l1 and l2:
        newhead = ListNode(None)
        cur = newhead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next		# cur 在每次选择完l1还是l2更新后需要移到新的节点更新
        cur.next = (l1 if l1 else l2)
        return newhead
    return l2 or l1
                
if __name__ == "__main__":
    l1 = ListNode(1)
    lp2 = ListNode(2)
    lp3 = ListNode(4)
    l1.next = lp2
    lp2.next = lp3

    l2 = ListNode(1)
    lp4 = ListNode(3)
    lp5 = ListNode(4)
    l2.next = lp4
    lp4.next = lp5

    l3 = mergeTwoLists(l2, l1)
    while l3:
        print(l3.val)
        l3 = l3.next
```

调试的时候发现没有写 cur = cur.next 导致cur的val始终是0没有更新。所以每次把新的节点加到cur链表的时候，一定要increment cur节点，不光要它指向新节点来增长链表，最后还要把cur站到新节点上。


### 141 Linked List Cycle

给了一个链表，看是否有环在里面

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

Follow up : can you solve it using *O(1)* (i.e. constant) memory?

分析: 需要判断的是节点是否被访问过

```python
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False    
        slow = fast = head   
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next   
            if fast == slow :
                return True
                
        return False
```

直接用龟兔赛跑的方法， 如果有环的话，快的那个一定可以在走完一圈或者两圈后追上慢的那个。如果没有环，快的会先跑到None，然后停止循环，输出False即可。


