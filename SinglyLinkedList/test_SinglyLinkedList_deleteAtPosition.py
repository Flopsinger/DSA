import pytest
from SinglyLinkedList import SinglyLinkedList

class Test_deleteAtPosition():
    def test_positionNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.deleteAtPosition(None)
    
    def test_positionGreaterLength(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.deleteAtPosition(0)

    def test_positionGreaterLength2(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        with pytest.raises(ValueError):
            SLL.deleteAtPosition(1)
    
    def test_positionNegative(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.deleteAtPosition(-1)
    
    def test_OneItemDeleteZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        assert SLL.deleteAtPosition(0) == 1
        assert SLL.head == None
    
    def test_twoItemsDeleteZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        assert SLL.deleteAtPosition(0) == 1
        assert SLL.head.data == 2
        assert SLL.head.nextNode == None
    
    def test_twoItemsDeleteOne(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        assert SLL.deleteAtPosition(1) == 2
        assert SLL.head.data == 1
        assert SLL.head.nextNode == None