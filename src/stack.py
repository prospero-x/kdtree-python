class Stack:
	def __init__(self):
		self.stack = []

	def pop(self):
		if not self.stack:
			return None
		return self.stack.pop()

	def push(self, value):
		self.stack.append(value)

	def peek(self):
		if not self.stack:
			return None
		return self.stack[-1]

	def empty(self):
		return len(self.stack) == 0
