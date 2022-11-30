import pytest
from SinglyLinkedList import SinglyLinkedList


class Test_insertBefore():
    def test_dataNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertBefore(None, 0)

    def test_beforeNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertBefore(0, None)

    def test_bothNone(self):
        SLL = SinglyLinkedList()
        with pytest.raises(ValueError):
            SLL.insertBefore(None, None)

    def test_OneItemInsertBeforeZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = True
        actual = SLL.insertBefore(2, 1)
        assert expected == actual

    def test_OneItemInsertBeforeNotInList(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = False
        actual = SLL.insertBefore(2, 2)
        assert expected == actual

    def test_TwoItemsInsertBeforeZero(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        expected = True
        actual = SLL.insertBefore(3, 1)
        assert expected == actual

    def test_TwoItemsInsertBeforeOne(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        expected = True
        actual = SLL.insertBefore(3, 2)
        assert expected == actual

    def test_TwoItemsInsertBeforeNotInList(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        SLL.append(2)
        expected = False
        actual = SLL.insertBefore(3, 3)
        assert expected == actual
