class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.insert(0, item)

	def dequeue(self):
		if self.size() != 0:
			return self.queue.pop()
		else:
			return None

	def size(self):
		return len(self.queue)

	def round(self, rounds):
		for i in range(rounds):
			x = self.dequeue()
			print("x", x)
			self.enqueue(x)
