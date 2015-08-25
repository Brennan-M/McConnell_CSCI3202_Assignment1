############################################
#		AI Homework Assignment One 		   #
############################################



# QUEUE IMPLEMENTATION #

from Queue import Queue as queue

class Queue(object):

	def __init__(self):
		self.q = queue(0)

	def put(self, num):
		if not isinstance(num, int):
			print ("Specified item is not an integer!")
			return False

		self.q.put(num)
		return True

	def get(self):
		if self.q.empty() == True:
			print ("The Queue is empty!")
			return None

		return self.q.get()

	def isEmpty(self):
		return self.q.empty()



# STACK IMPLEMENTATION #

class Stack(object):

	def __init__(self):
		self.stack = []

	def push(self, data):
		if not isinstance(data, int):
			print ("Specified item is not an integer!")
			return False

		self.stack.append(data)
		return True

	def pop(self):
		if (len(self.stack) <= 0):
			print ("The Stack is empty!")
			return None
			
		return self.stack.pop()

	def checkSize(self):
		return len(self.stack)





#############################################

if __name__ == "__main__":

	# TESTING QUEUE IMPLEMENTATION #

	testQueue = Queue()
	testQueue.put(5)
	testQueue.put('hi')
	testQueue.put(19)
	print testQueue.get()
	print testQueue.get()
	print testQueue.get()

	# TESTING STACK IMPLEMENTATION #

	testStack = Stack()
	testStack.push(5)
	testStack.push(3.23)
	testStack.push(567)
	print testStack.checkSize()
	print testStack.pop()
	print testStack.pop()
	print testStack.pop()

