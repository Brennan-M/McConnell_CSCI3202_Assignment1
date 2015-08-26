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


# BINARY TREE IMPLEMENTATION #

class Node(object):

	def __init__(self, data, left = None, right = None, parent = None):

		self.val = None
		valid = self.setVal(data)
		if not valid:
			return None

		self.parent = None
		valid = self.setParent(parent)
		if not valid:
			return None

		self.left = None
		valid = self.setLeft(left)
		if not valid:
			return None

		self.right = None
		valid = self.setRight(right)
		if not valid:
			return None

	def setVal(self, data):
		if not isinstance(data, int):
			print ("Node data is not of type int!")
			return False

		self.val = data
		return True

	def setLeft(self, lNode):
		if not isinstance(lNode, Node):
			print ("Left node is not of type Node!")
			return False

		self.left = lNode
		return True

	def setRight(self, rNode):
		if not isinstance(rNode, Node):
			print ("Right node is not of type Node!")
			return False

		self.left = rNode
		return True

	def setParent(self, pNode):
		if not isinstance(pNode, Node):
			print ("Parent node is not of type Node!")
			return False

		self.parent = pNode
		return True

	def getVal(self):
		return self.val

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getParent(self):
		return self.parent




class BinaryTree(object):

	def __init__(self, rootValue):

		self.root = Node(rootValue)
		if (self.root == None):
			return None

		self.existingNodes = {self.root.val : self.root}


	def add(self, value, parentValue):
		if not (self.existingNodes.has_key(parentValue)):
			print ("Parent not found!")
			return False

		# Directions were a bit unclear, so I chose to make duplicates an impossibility
		if (self.existingNodes.has_key(value)):
			print ("This node already exists in our tree!")
			return False

		pNode = self.existingNodes[parentNode.val]
		newNode = Node(value)
		if (newNode == None):
			print ("Unable to add this node, type error occured")
			return False

		if (pNode.getLeft == None):
			self.existingNodes[value] = newNode
			pNode.setLeft(newNode)
		elif (pNode.getRight == None):
			self.existingNodes[value] = newNode
			pNode.setRight(parentValue)
		else:
			print ("Parent already has two children, node not added.")
			return False

		return True






#############################################

if __name__ == "__main__":

	# TESTING QUEUE IMPLEMENTATION #

	print ("		Testing Queue Implementation		")
	print ("--------------------------------------------")
	print ()

	testQueue = Queue()
	testQueue.put(5)
	testQueue.put('hi')
	testQueue.put(19)
	print testQueue.get()
	print testQueue.get()
	print testQueue.get()

	# TESTING STACK IMPLEMENTATION #

	print ("		Testing Stack Implementation		")
	print ("--------------------------------------------")
	print ()

	testStack = Stack()
	testStack.push(5)
	testStack.push(3.23)
	testStack.push(567)
	print testStack.checkSize()
	print testStack.pop()
	print testStack.pop()
	print testStack.pop()

	# TESTING BINARY TREE IMPLEMENTATION #
 
	print ("	 Testing Binary Tree Implementation 	")
	print ("--------------------------------------------")
	print ()

	testBinTree = BinaryTree(7)
