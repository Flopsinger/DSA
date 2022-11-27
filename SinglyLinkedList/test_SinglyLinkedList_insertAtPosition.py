import pytest
from SinglyLinkedList import SinglyLinkedList

class Test_insertAtPosition():
    def test_dataNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAtPosition(None, 0)
    
    def test_positionNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAtPosition(0, None)
    
    def test_positionNegative(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAtPosition(0, -1)
    
    def test_oneItemInsertZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = True
        SLL.insertAtPosition(2, 0)
        assert SLL.head.data == 2
        assert SLL.head.nextNode.data == 1

    def test_oneItemInsertOne(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.insertAtPosition(2, 1)
        assert SLL.head.data == 1
        assert SLL.head.nextNode.data == 2
    
    def test_twoItemsInsertZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        SLL.insertAtPosition(3, 0)
        assert SLL.head.data == 3
        assert SLL.head.nextNode.data == 1
    
    def test_twoItemsInsertOne(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        SLL.insertAtPosition(3, 1)
        assert SLL.head.data == 1
        assert SLL.head.nextNode.data == 3
        assert SLL.head.nextNode.nextNode.data == 2
        
    def test_twoItemsInsertTwo(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        SLL.insertAtPosition(3, 2)
        assert SLL.head.data == 1
        assert SLL.head.nextNode.data == 2
        assert SLL.head.nextNode.nextNode.data == 3

    def test_positionGreaterLength(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAtPosition(1, 1)