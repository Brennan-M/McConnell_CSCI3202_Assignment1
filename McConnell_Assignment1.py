############################################
#		AI Homework Assignment One 		   #
############################################

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



#############################################

if __name__ == "__main__":

	# TESTING QUEUE IMPLEMENTATION
	testQueue = Queue()
	testQueue.put(5)
	testQueue.put('hi')
	testQueue.put(19)
	print testQueue.get()
	print testQueue.get()
	print testQueue.get()
