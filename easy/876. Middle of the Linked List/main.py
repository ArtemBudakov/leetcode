from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, value):
        new_node = ListNode(val=value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
        return self


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow_node: ListNode = head
        fast_node: ListNode = head
        while True:
            if fast_node.next is None:
                return slow_node
            elif fast_node.next.next is None:
                return slow_node.next

            slow_node = slow_node.next
            fast_node = fast_node.next.next


def test(linked_list: LinkedList):
    head = linked_list.head
    element = head

    while True:
        if element.next is None:
            print(element.val, element.next)
            break
        print(element.val, element.next.val)
        element = element.next


if __name__ == '__main__':
    base_list = [1, 2, 3, 4, 5]

    ll1 = LinkedList()
    for el in base_list:
        ll1.append(el)
    test(ll1)
    s1 = Solution()
    result = s1.middleNode(head=ll1.head)
    print(result.val)

    base_list = [1, 2, 3, 4, 5, 6]

    ll1 = LinkedList()
    for el in base_list:
        ll1.append(el)
    test(ll1)
    s1 = Solution()
    result = s1.middleNode(head=ll1.head)
    print(result.val)
