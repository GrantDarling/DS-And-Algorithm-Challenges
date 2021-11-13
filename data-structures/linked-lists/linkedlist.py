class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next 


class LinkedList():
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)

		if(self.head):
			current = self.head
			while(current.next):
				current = current.next
			current.next = new_node
			return 

		self.head = new_node

	def remove(self, key):
		current = self.head 

		if(current):
			if(current.data == key):
				self.head = current.next
				current = None
				return

			while(current.next):
				if(current.data == key):
					break
				prev = current 
				current = current.next

		if(current == None):
			return 

		prev.next = current.next 
		current = None
					
		

	def printLL(self):
		while(self.head):
			print(self.head.data)
			self.head = self.head.next
			

LL = LinkedList()
LL.insert(5)
LL.insert(6)
LL.insert(7)
LL.remove(5)
LL.printLL()