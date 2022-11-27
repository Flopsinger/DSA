from SinglyLinkedList import SinglyLinkedList


class Test_prepend:
    def test_empty(self):
        SLL = SinglyLinkedList()
        SLL.prepend(1)
        assert SLL.head.data == 1
        assert SLL.head.nextNode is None

    def test_oneItem(self):
        SLL = SinglyLinkedList()
        SLL.prepend(1)
        SLL.prepend(2)
        assert SLL.head.data == 2
        assert SLL.head.nextNode.data == 1
