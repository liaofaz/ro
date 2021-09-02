class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        在此处初始化数据结构
        """
        self.__head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        获取链表中第th个节点的索引值。如果索引无效，则返回-1
        """
        i = 0
        node = self.__head
        while node:
            if index == i:
                return node.val
            node = node.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        在链表的第一个元素之前添加值为val的节点。插入后，新节点将成为链表的第一个节点
        """
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        将值为val的节点附加到链表的最后一个元素
        """
        node = Node(val)
        cur = self.__head
        if cur is None:
            self.__head = node
            return
        while cur.next:
            cur = cur.next
        cur.next = node

    def addAtIndex(self, index: int, val: int) -> int:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        在链表的索引节点之前添加一个值为val的节点。如果索引等于链表的长度，则节点将附加到链表的末尾。如果索引大于长度，则不会插入节点。
        """
        cou = 0
        cur = self.__head
        while cur:
            cou += 1
            cur = cur.next
        if index <= 0:
            self.addAtHead(val)
        elif index == cou:
            self.addAtTail(val)
        elif index > cou:
            return -1
        else:
            node = Node(val)
            cur = self.__head
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def deleteAtIndex(self, index: int) -> int:
        """
        Delete the index-th node in the linked list, if the index is valid.
        如果索引有效，请删除链表中的第th个节点
        """
        if index < 0:
            return -1
        elif index == 0:
            if self.__head is None:
                return -1
            elif self.__head.next:
                self.__head = self.__head.next
            else:
                self.__head = None
        else:
            cur = self.__head
            i = 0
            while cur:
                i += 1
                # 此时 cur 是index的上一个结点
                if index == i and cur.next:
                    if cur.next.next:
                        cur.next = cur.next.next
                    elif cur.next:
                        cur.next = None
                    else:
                        return -1
                cur = cur.next

    def item(self):
        cur = self.__head
        while cur:
            yield cur.val
            cur = cur.next

# Your MyLinkedList object will be instantiated and called as such:
# 您的MyLinkedList对象将被实例化并按此方式调用

# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
print(list(obj.item()))
print(obj.get(5))
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)
