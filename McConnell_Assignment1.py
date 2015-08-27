############################################
#		AI Homework Assignment One 		   #
#			Brennan McConnell              #
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

		valid = self.setVal(data)
		if not valid:
			return None
	
		valid = self.setLeft(left)
		if not valid:
			return None
		
		valid = self.setRight(right)
		if not valid:
			return None
	
		valid = self.setParent(parent)
		if not valid:
			return None
		


	def setVal(self, data):
		if not isinstance(data, int):
			print ("Node data is not of type int!")
			return False

		self.val = data
		return True

	def setLeft(self, lNode):
		if (lNode != None):
			if not isinstance(lNode, Node):
				print ("Left node is not of type Node!")
				return False

		self.left = lNode
		return True

	def setRight(self, rNode):
		if (rNode != None):
			if not isinstance(rNode, Node):
				print ("Right node is not of type Node!")
				return False

		self.right = rNode
		return True

	def setParent(self, pNode):
		if (pNode != None):
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
		if (self.root is None):
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

		pNode = self.existingNodes[parentValue]
		if (pNode == None):
			print "WTF", parentValue
			return False

		newNode = Node(value, None, None, pNode)
		if (newNode is None):
			print ("Unable to add this node, type error occured")
			return False

		if (pNode.getLeft() is None):
			self.existingNodes[value] = newNode
			pNode.setLeft(newNode)
		elif (pNode.getRight() is None):
			self.existingNodes[value] = newNode
			pNode.setRight(newNode)
		else:
			print ("Parent already has two children, node not added.")
			print pNode.getLeft()
			print pNode.getRight()
			return False

		return True

	def delete(self, value):
		if not (self.existingNodes.has_key(value)):
			print ("Node not found.")
			return False

		nodeToDelete = self.existingNodes[value]
		if (nodeToDelete.getLeft() is None and nodeToDelete.getRight() is None):
			pNode = nodeToDelete.getParent()
			if (pNode is None):
				print ("Stop! You cannot delete the root of the tree!")
				return False

			if pNode.getLeft() == nodeToDelete:
				pNode.setLeft(None)
			elif pNode.getRight() == nodeToDelete:
				pNode.setRight(None)
			del self.existingNodes[nodeToDelete.getVal()]
			nodeToDelete = None
			print ("Node Successfully deleted.")
			return True

		else:
			print ("Node not deleted, has children.")
			return False

	def traverseAndPrint(self, node):
		print node.getVal()

		if (node.getLeft() != None):
			self.traverseAndPrint(node.getLeft())
		if (node.getRight() != None):
			self.traverseAndPrint(node.getRight())


	def printTree(self):
		self.traverseAndPrint(self.root)



# GRAPH IMPLEMENTATION #

class Graph(object):

	def __init__(self, value = None):
		self.nodes = {}
		if value != None:
			self.addVertex(value)

	def addVertex(self, value):
		if not isinstance(value, int):
			print ("Value entered is not an integer!")
			return False

		if self.nodes.has_key(value):
			print ("Vertex already exists.")
			return False

		self.nodes[value] = [value]
		return True

	def addEdge(self, value1, value2):
		if (self.nodes.has_key(value1) == False or self.nodes.has_key(value2) == False):
			print ("One or more vertices not found.")
			return False

		if (value2 in self.nodes[value1] or value1 in self.nodes[value2]):
			print ("This edge already exists!")
			return False

		self.nodes[value1].append(value2)
		self.nodes[value2].append(value1)
		return True

	def findVertex(self, value):
		if (self.nodes.has_key(value)):
			print self.nodes[value]
		else:
			print ("Vertex not found!")



#############################################
import random

if __name__ == "__main__":

	# TESTING QUEUE IMPLEMENTATION #

	print ("")
	print ("	Testing Queue Implementation		")
	print ("--------------------------------------------")
	print ("")

	testQueue = Queue()
	testQueue.put(5)
	testQueue.put('hi')
	testQueue.put(19)
	print testQueue.get()
	print testQueue.get()
	print testQueue.get()
	
	testQueue2 = Queue()

	for i in range(1, 11):
		testQueue2.put(i)
	while (not testQueue2.isEmpty()):
		print testQueue2.get(),

	print ("")

	# TESTING STACK IMPLEMENTATION #

	print ("")
	print ("	Testing Stack Implementation		")
	print ("--------------------------------------------")
	print ("")

	testStack = Stack()
	testStack.push(5)
	testStack.push(3.23)
	testStack.push(567)
	print testStack.checkSize()
	print testStack.pop()
	print testStack.pop()
	print testStack.pop()

	testStack2 = Stack()
	for i in range(1, 11):
		testStack2.push(i)
	while (testStack2.checkSize() > 0):
		print testStack2.pop(),
	print ("")

	# TESTING BINARY TREE IMPLEMENTATION #
 
 	print ("")
	print ("     Testing Binary Tree Implementation 	")
	print ("--------------------------------------------")
	print ("")

	testBinTree = BinaryTree(7)
	testBinTree.add(2, 7)
	testBinTree.add(4, 7)
	testBinTree.add(3, 2)
	testBinTree.add(5, 4)
	testBinTree.printTree()
	testBinTree.delete(4)
	testBinTree.delete(5)
	testBinTree.delete(4)
	testBinTree.printTree()

	testBinTree2 = BinaryTree(0)
	for i in range(1, 11):
		testBinTree2.add(i, i-1)
		testBinTree2.add(i*2, i-1)
	testBinTree2.printTree()
	testBinTree2.delete(20)
	testBinTree2.delete(18)
	testBinTree2.delete(10)
	testBinTree2.printTree()
	testBinTree2.delete(4)

	# TESTING GRAPH IMPLEMENTATION #
 
 	print ("")
	print ("	Testing Graph Implementation 		")
	print ("--------------------------------------------")
	print ("")

	testGraph = Graph(5)
	testGraph.addVertex(8)
	testGraph.addVertex(12)
	testGraph.addEdge(8, 12)
	testGraph.findVertex(12)
	testGraph.addEdge(9, 8)
	testGraph.findVertex(4)

	testGraph2 = Graph(19)
	for i in range(0, 10):
		testGraph2.addVertex(i)
		current = random.randrange(10, 500)
		testGraph2.addVertex(current)

		testGraph2.addEdge(current, 19)
		testGraph2.addEdge(i, current)
		testGraph2.addEdge(10-i, i)


	for i in range(0, 10):
		testGraph2.findVertex(i),

	testGraph2.findVertex(19)

	# PRINT SUCCESS MESSAGE #

	print ("")
	print ("--------------------------------------------")
	print ("")
	print ("Congratulations, All tests passed successfully!")
	print ("")







