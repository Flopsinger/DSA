import pytest
from SinglyLinkedList import SinglyLinkedList


class Test_insertAfter:
    def test_dataNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAfter(None, 0)

    def test_afterNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAfter(0, None)

    def test_bothNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertAfter(None, None)

    def test_emptyList(self):
        SLL = SinglyLinkedList()
        expected = False
        actual = SLL.insertAfter(1, 1)
        assert expected == actual

    def test_oneItem(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = True
        actual = SLL.insertAfter(2, 1)
        assert expected == actual

    def test_oneItemNotInList(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = False
        actual = SLL.insertAfter(3, 2)
        assert expected == actual

    def test_betweenTwoItems(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        expected = True
        actual = SLL.insertAfter(3, 1)
        assert expected == actual
