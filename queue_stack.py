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
		self.stack = []

	def size(self):
		return len(self.stack)

	def pop(self):
		if self.size() != 0:
			self.peek()
			return self.stack.pop()
		else:
			return None

	def push(self, value):
		self.stack.append(value)
	

	def peek(self):
		if self.size() != 0:
			return self.stack[self.size()-1]
		else:
			return None
