from SinglyLinkedList import SinglyLinkedList
import pytest


class Test_append:
    def test_empty(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        assert SLL.head.data == 1

    def test_OneItem(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        assert SLL.head.data == 1
        assert SLL.head.nextNode.data == 2
