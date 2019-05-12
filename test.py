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
            cur = cur.next
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

