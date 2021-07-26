from typing import List
from icecream import ic


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode):
        """68ms,15MB 链表->数字->求和->链表

        Args:
            l1 (ListNode): [description]
            l2 (ListNode): [description]

        Returns:
            [type]: [description]
        """
        ln1val = 0
        i = 0
        while l1 != None:
            ln1val += l1.val * (10**i)
            l1 = l1.next
            i += 1
        ln2val = 0
        i = 0
        while l2 != None:
            ln2val += l2.val * (10**i)
            l2 = l2.next
            i += 1
        val = ln1val + ln2val
        l3 = list(reversed(list(map(int, str(val)))))
        ln3 = ListNode(l3[-1])
        for i in range(len(l3) - 1, 0, -1):
            ln3 = ListNode(l3[i - 1], ln3)
        return ln3

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode):
        """56ms,15.1MB

        Args:
            l1 (ListNode): [description]
            l2 (ListNode): [description]

        Returns:
            [type]: [description]
        """
        jinwei = 0
        l3 = []
        while 1:
            if l1 is None and l2 is None and jinwei == 0:  #在判断中is None or ==0没必要写
                break
            if l1 is None and l2 is not None:
                val = l2.val + jinwei
            elif l2 is None and l1 is not None:
                val = l1.val + jinwei
            elif l2 is None and l1 is None:
                val = jinwei
            else:
                val = l1.val + l2.val + jinwei

            if val > 9:
                jinwei = 1
                l3.append(val - 10)
            else:
                jinwei = 0
                l3.append(val)

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next
        ln3 = ListNode(l3[-1])
        for i in range(len(l3) - 1, 0, -1):
            ln3 = ListNode(l3[i - 1], ln3)
        return ln3

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode):
        """52ms,14.9MB"""
        head = curr = ListNode()
        carry = val = 0  #多一个val的变量用来把carry==1的情况从和l1.val的相加中取出来

        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.val + val  #同时，没有先后顺序
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)  #前者是商，后者是余数
            curr.next = curr = ListNode(
                val)  #先进行curr.next=ListNode()，在进行curr=ListNode()

        return head.next

    def addTwoNumbers4(self, l1: ListNode, l2: ListNode):
        """补0解法，目前最快:48ms,15.1MB"""
        h1, h2 = l1, l2
        tmp = 0
        while h1 or h2:  # 需要遍历最长的数
            val = h1.val + h2.val + tmp  # 值=l1 + l2 +进位
            h1.val, tmp = val % 10, val // 10
            if not h1.next and h2.next: h1.next = ListNode(0)  # 如果l1太短，添节点0
            if not h2.next and h1.next: h2.next = ListNode(0)  # 如果l2太短，添节点0
            if not h1.next and not h2.next:  # 如果两个一样短，判断是否有进位，有就添节点
                if tmp: h1.next = ListNode(tmp)
                return l1  # 两个一样短的时候必然是返回的时候
            h1 = h1.next
            h2 = h2.next


def main():
    l1 = [9, 1, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    ln1 = ListNode(l1[-1])
    for i in range(len(l1) - 1, 0, -1):
        ln1 = ListNode(l1[i - 1], ln1)
    ln2 = ListNode(l2[-1], None)
    for i in range(len(l2) - 1, 0, -1):
        ln2 = ListNode(l2[i - 1], ln2)
    s = Solution()
    ic(s.addTwoNumbers3(ln1, ln2))


if __name__ == "__main__":
    main()