from SinglyLinkedList import SinglyLinkedList
import pytest

class Test_deleteLast:
    def test_empty(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.deleteLast()
    
    def test_OneItem(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        assert SLL.deleteLast() == 1

    def test_TwoItems(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        assert SLL.deleteLast() == 2
    
    def test_ThreeItems(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        SLL.append(3)
        assert SLL.deleteLast() == 3