
class LinkedStack:

	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self, e, n):
			self._element = e
			self._next = n 

	def __init__(self):
		self._head = None
		self._size = 0 
	
	def __len__(self):
		return self._size 

	def is_empty(self):
		return self._size == 0

	def push(self, e):
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._head._element 

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty.')
		res = self._head._element 
		self._head = self._head._next
		self._size -= 1 
		return res 

def main():
	l = LinkedStack()
	for i in range(10):
		l.push(i)

	while l.is_empty() != True:
		print(l.pop(), ' ')

if __name__ == '__main__':
	main()

