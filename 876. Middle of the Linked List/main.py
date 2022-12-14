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

        list_of_nodes = self.get_all_nodes(head)

        if len(list_of_nodes) % 2 == 1:
            result = list_of_nodes[len(list_of_nodes) // 2]
        else:
            result = list_of_nodes[len(list_of_nodes) // 2]
        return result

    def get_all_nodes(self, head: ListNode):
        nodes_list: list = []
        node: ListNode = head

        while True:
            if node.next is None:
                nodes_list.append(node)
                break
            nodes_list.append(node)
            node = node.next
        return nodes_list


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

    # ll1.append('a')
    # ll1.append('b')
    # ll1.append('c')
    # test(ll1)
