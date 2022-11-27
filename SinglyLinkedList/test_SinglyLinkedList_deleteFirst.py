from SinglyLinkedList import SinglyLinkedList
import pytest

class Test_deleteFirst:
    def test_empty(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.deleteFirst()
    
    def test_OneItem(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        assert SLL.deleteFirst() == 1
    
    def test_TwoItems(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        assert SLL.deleteFirst() == 1