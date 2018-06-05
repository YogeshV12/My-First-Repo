class yogi:

	def __init__(self1, data2):
		self1.data3 = data2
		self1.next = None

class LinkedList:

	def __init__(self1):
		self1.head = None

	def printL(self1):
		temp = self1.head
		print("Hello")
		while(temp):
			print (temp.data3)
			temp = temp.next

if __name__=='__main__':

	list2 = LinkedList()

	list2.head = yogi(1)
	sec = yogi(2)
	thrd = yogi(3)

	list2.head.next = sec;
	sec.next = thrd;

	list2.printL()
