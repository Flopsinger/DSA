from SinglyLinkedList import SinglyLinkedList

SLL = SinglyLinkedList()

for i in range(10):
    SLL.append(i)

SLL.prepend(-1)

print(SLL.getLength())

print(SLL.deleteFirst())

print(SLL.deleteLast())

SLL.print()
