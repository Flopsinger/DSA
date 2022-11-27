class SinglyLinkedList:
    head = None
    def __init__(self):
        self.head = None

    # Tests 2/2 
    def append(self, data) -> None:
        """Appends a new Node with the given data to the end of the list.

        Args:
            data (any): Data of the new Node

        Speed: 
            Always: O(n)
        """
        current = self.head
        newNode = Node(data)
        if current == None:
            self.head = newNode
        else:
            while current.nextNode:
                current = current.nextNode
            current.nextNode = newNode
    
    def print(self) -> None:     
        """
        Prints the all items in the list sequentially separated by dashes "-"
        
        Speed: 
            Always O(n)
        """
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.nextNode
        print()
        
    # Tests 2/2
    def prepend(self, data) -> None:
        """Prepends a new Node with the given data to the beginning of the list.

        Args:
            data (any): Data of the new Node
        
        Speed:
            Always: O(1)
        """
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    # Tests 2/2
    def getLength(self) -> int:
        """Gets the length of the List

        Returns:
            int: Amount of Nodes in the List

        Speed:
            Always: O(n)
        """
        count = 0
        current = self.head
        if current == None:
            return count
        else:
            count += 1
            while current.nextNode:
                count += 1
                current = current.nextNode
        return count
    
    # Tests 3/3
    def deleteFirst(self) -> any:
        """Deletes the first Node from the list.

        Returns:
            any: Data of the first Node
        
        Speed:
            Always: O(1)
        """
        firstNode = self.head
        if not firstNode:
            raise ValueError("No Nodes in the List")
        self.head = firstNode.nextNode
        data = firstNode.data
        firstNode = None
        return data

    # Tests 4/4
    def deleteLast(self) -> any:
        """Deletes the last Node from the list.

        Returns:
            any: Data of the last Node
        
        Speed:
            Always: O(n)
        """
        current = self.head
        if not current:
            raise ValueError("No Nodes in the List")
        elif not current.nextNode:
            data = current.data
            self.head = None
            return data
        else:
            nextNode = current.nextNode
            while nextNode.nextNode: 
                current = nextNode
                nextNode = nextNode.nextNode
            data = nextNode.data
            nextNode = None
            current.nextNode = None
            return data 

    # Tests 2/2
    def isEmpty(self) -> bool:
        """Checks if the List is empty

        Returns:
            bool: List is Empty
        """
        if self.head:
            return False
        return True

    # Tests 7/7
    def insertAfter(self, data, after) -> bool:
        """Inserts a Node after another node.

        Args:
            data (any): Data of the new Node
            after (any): Data of the other Node

        Raises:
            ValueError: Data is None
            ValueError: After is None

        Returns:
            bool: Insert succesful

        Speed:
            Best:  O(1) (Insert after Node0)
            Worst: O(n) (Insert after Last Node)
        """
        if not data:
            raise ValueError("Data can not be None")
        if not after:
            raise ValueError("After can not be None")
        if self.isEmpty():
            return False
        current = self.head
        while current.nextNode and current.data != after:
            current = current.nextNode
        if current.data == after:
            newNode = Node(data)
            newNode.nextNode = current.nextNode
            current.nextNode = newNode
            return True
        return False

    # 0/X
    def insertAtPosition(self, data, position):
        

class Node:
    nextNode = None
    data = None
    def __init__(self, data):
        self.data = data