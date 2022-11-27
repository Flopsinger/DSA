from SinglyLinkedList import SinglyLinkedList


class Test_isEmpty:
    def test_empty(self):
        SLL = SinglyLinkedList()
        expected = True
        actual = SLL.isEmpty()
        assert expected == actual

    def test_oneItem(self):
        SLL = SinglyLinkedList()
        SLL.append(1)
        expected = False
        actual = SLL.isEmpty()
        assert expected == actual
