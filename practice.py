import sys 

class Stack:
	def __init__(self):
		self.stack = []
	def isEmpty():
		return self.stack == []
	def push(self,data):
		self.stack.append(data)
	def pop(self):
		return self.stack.pop() 
	def peek(self):
		return self.stack[len(self.stack) - 1]
	def size(self):
		return len(self.stack)

class Queue:
	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None] * Queue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		res = self._data[self._front]
		self._data[self._front] = None 
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return res 

	def enqueue(self, e):
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size += 1

	def _resize(self, cap):
		old = self._data 
		self._data = [None] * cap 
		cur = self._front 
		for k in range(self._size):
			self._data[k] = old[cur]
			cur = (cur + 1) % len(old)
		self._front = 0


class Node:
	def __init__(self,val):
		self.val = val 
		self.next = None

class LinkedList:
	def __init__(self):
		self._head = None 
		self._tail = None 
	
	def insert_head(self,data):
		new_Node = Node(self,data)
		new_Node.next = self._head 
		self._head = new_Node

	def print_list(self):
		if self.__head == None:
			print("Empty List")
		else:
			p = self.__head 
			while p is not None:
				print(n.val, " ")
				p = p.next 


def max(arr):
	length = len(arr)
	for i in range(0,length - 1):
		if arr[i] > arr[i+1]:
			tmp = arr[i]
			arr[i] = arr[i + 1]
			arr[i+1] = tmp 
	maxVal = arr[length - 1]
	return maxVal

def min(arr):
	length = len(arr)
	for i in range(0,length - 1):
		if arr[i] < arr[i+1]:
			tmp = arr[i]
			arr[i] = arr[i + 1]
			arr[i+1] = tmp 
	minVal = arr[length - 1]
	return minVal

def bubble_sort(arr):
	length = len(arr)
	for i in range(0, length - 1):
		for j in range(0, length - i - 1):
			if arr[j] > arr[j + 1]:
				tmp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = tmp

def reverse(arr):
	length = len(arr)
	for i in range(0, int(length / 2)):
		tmp = arr[i]
		arr[i] = arr[length - i - 1]
		arr[length - i - 1] = tmp 

def binary_search(arr, target):
	length = len(arr)
	low = 0 
	high = length - 1 
	while low <= high:
		mid = low + (high - low) // 2
		if arr[mid] == target:
			return mid 
		elif target < arr[mid]:
			high = mid - 1
		elif target > arr[mid]: 
			low = mid + 1

	return -1 



def main():
	scores = [60,50,89,105,70]
	maxVal = max(scores)
	print("Max value of the list is: ", maxVal)
	minVal = min(scores)
	print("Max value of the list is: ", minVal)
	print("Sorting list using bubble sort . . .")
	bubble_sort(scores)
	for score in scores:
		print(score)
	print("Reversing list . . .")
	reverse(scores)
	for score in scores:
		print(score)
	print("Searching for the value 50 using binary search . . .")
	target = binary_search(scores, 50)
	print("Result: ", scores[target])

	print("Constructing a list . . .")
	s = Stack()
	s.push(10)
	s.push(20)
	s.push(30)
	s.push(40)
	for i in range(1, s.size()):
		print(s.pop(), " ")
	

	q = Queue()
	for k in range(1,10):
		q.enqueue(k)
	while q.is_empty() != True:
		print(q.dequeue(), " ")
	


if __name__ == "__main__":
	main()
