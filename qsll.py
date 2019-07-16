class Queue:
	def __init__(self):
		self.inbox = Stack()
		self.outbox = Stack()

	def enqueue(self, item):
		self.inbox.push(item)

	def dequeue(self):
		if self.outbox.size() != 0:
			return self.outbox.pop()
		elif self.inbox.size() != 0:
			x = self.inbox.pop()
			while x is not None:
				self.outbox.push(x)
				x = self.inbox.pop()
			return self.outbox.pop()
		else:
			return None

	def inbox_size(self):
		return (self.inbox.size())

	def outbox_size(self):
		return (self.outbox.size())

class Stack:
	def __init__(self):
		self.stack = LinkedList2()

	def size(self):
		return self.stack.len()

	def pop(self):
		if self.size() != 0:
			popped = self.stack.tail.value
			if self.stack.tail is not self.stack.head:
				self.stack.tail.prev.next = None
				self.stack.tail = self.stack.tail.prev
			elif self.stack.tail is self.stack.head:
				self.stack.clean()
			return popped
		else:
			return None

	def push(self, value):
		self.stack.add_in_tail(Node(value))
	

	def peek(self):
		if self.size() != 0:
			return self.stack.tail
		else:
			return None

class Node:
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class LinkedList2:  
	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def find(self, val):
		currentNode = self.head
		if self.head is None:
			return None
		while currentNode is not None:
			if currentNode.value == val:
				return currentNode
			else:
				currentNode = currentNode.next
		return None
		
	def find_all(self, val):
		currentNode = self.head
		listOfNodes = []
		if self.head is None:
			return None
		while currentNode is not None:
			if currentNode.value == val:
				listOfNodes.append(currentNode)
			currentNode = currentNode.next
		if len(listOfNodes) == 0:
			return None
		return listOfNodes

	def delete(self, val, all=False):
		currentNode = self.head
		previousNode = None
		if self.head is None:
			return
		else:
			if self.head.value == val:
				if self.len() == 1:
					self.head = None
					self.tail = None
					return
				else:
					currentNode = self.head.next
					self.head = currentNode
					currentNode.prev = None
					if all==False:
						return
		if all==False:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					else:
						currentNode.next.prev = previousNode
					return
				else:
					previousNode = currentNode
					currentNode = currentNode.next
			return
		else:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					else:
						currentNode.next.prev = previousNode
					currentNode = currentNode.next
				else:
					previousNode = currentNode
					currentNode = currentNode.next

	def clean(self):
		self.head = None
		self.tail = None
		
	def len(self):
		currentNode = self.head
		nodeCount = 0
		while currentNode is not None:
			nodeCount += 1
			currentNode = currentNode.next
		return nodeCount

	def insert(self, afterNode, newNode):
		if self.len() == 0:
			self.add_in_tail(newNode)
		else:
			currentNode = self.head
			while currentNode is not None:
				if currentNode is afterNode:
					newNode.next = currentNode.next
					currentNode.next = newNode
					newNode.prev = currentNode
					newNode.next.prev = newNode
					if currentNode is self.tail:
						self.tail = newNode
					return
				else:
					currentNode = currentNode.next
			if currentNode is None:
				self.add_in_tail(newNode)

	def add_in_head(self, newNode):
		if self.head is None:
			self.head, self.tail = newNode, newNode
			newNode.prev, newNode.next = None, None
		else:
			self.head.prev, newNode.next = newNode, self.head
			self.head = newNode
			newNode.prev = None

	def delete_head(self):
		if self.head is not None:
			if self.head is self.tail:
				self.clean()
			else:
				self.head.next.prev = None
				self.head = self.head.next

	def delete_tail(self):
		if self.tail is not None:
			if self.head is self.tail:
				self.clean()
			else:
				self.tail.prev.next = None
				self.tail = self.tail.prev    

l = LinkedList2()
l.add_in_tail(Node(11))
l.add_in_tail(Node(12))
print(l.len())
print("HEAD", l.head.value)
print("TAIL", l.tail.value)
l.delete_tail()
print(l.len())
print("HEAD", l.head.value)
print("TAIL", l.tail.value)
