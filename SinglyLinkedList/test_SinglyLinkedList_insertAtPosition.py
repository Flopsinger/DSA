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