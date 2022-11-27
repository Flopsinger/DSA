from SinglyLinkedList import SinglyLinkedList
import pytest

class Test_getLength:
    def test_positive(self):
        SLL = SinglyLinkedList()
        for i in range(10):
            SLL.append(i)
        assert SLL.getLength() == 10

    def test_zero(self):
        SLL = SinglyLinkedList()
        assert SLL.getLength() == 0