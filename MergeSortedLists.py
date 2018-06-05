class yogi:
	def __init__(self1, data2):
		self1.data3 = data2
		self1.next = None

class rajjo:
	def __init__(self,data4):
		self.data3 = data4
		self.next = None

class LinkedList:

	def __init__(self2):
		self2.head = None

	def printL(self3):
		temp = self3.head
		while(temp):
			print (temp.data3)
			temp = temp.next

	def length(self5):
		item = self5.head
		return self5.length3(item)

	def length3(self5,item):
		if(item == None):
			return 0
		else:
			return 1+self5.length3(item.next) 

	def swap(self,first,second):
		if(first==self.head):
			secprev = self.head
			while(secprev.next != second) :
				secprev = secprev.next
			# secprev.next = first
			# self.head = second
			# first.next, second.next = second.next, first.next
			self.head = second
			secprev.next = first

			temp = first.next
			first.next = second.next
			second.next = temp

		else:
			firprev = self.head
			while(firprev.next!=first):
				firprev = firprev.next

			secprev = self.head
			while(secprev.next!=second):
				secprev = secprev.next

			
			temp = firprev.next
			firprev.next = secprev.next
			secprev.next = temp

			temp = first.next
			first.next = second.next
			second.next = temp

	def returnIth(self,i):
		temp = self.head
		while(i>0):
			temp = temp.next
			i-=1
		return temp

	def reverseList(self):
		temp = self.head
		N = self.length()
		m = 0
		n = N/2
		while(n):
			self.swap(self.returnIth(m),self.returnIth(N-m-1))
			m+=1
			n-=1

	def MergeSorted(self, headOf2):
		temp1 = self.head
		temp2 = headOf2
		newlist = LinkedList()
		if(temp1.data3<temp2.data3):
			newlist.head = temp1
			temp1 = temp1.next
		else:
			newlist.head = temp2
			temp2 = temp2.next
		temp3 = newlist.head

		while(temp1 and temp2):
			if(temp1.data3<temp2.data3):
				temp3.next = temp1
				temp1 = temp1.next
				temp3 = temp3.next
			elif(temp1.data3>temp2.data3):
				temp3.next = temp2
				temp2 = temp2.next
				temp3 = temp3.next
			else:
				temp3.next = temp1
				temp3 = temp3.next
				temp1 = temp1.next
				temp3.next = temp2
				temp2 = temp2.next
				temp3 = temp3.next
		return newlist


list2 = LinkedList()

list2.head = yogi(11)
sec = yogi(22)
thrd = yogi(33)
f4 = yogi(44)
f5 = yogi(55)
f6 = yogi(66)

list2.head.next = sec
sec.next = thrd
thrd.next = f4
f4.next = f5
f5.next = f6

list3 = LinkedList()
list3.head = rajjo(15)
S2 = rajjo(25)
S3 = rajjo(33)
S4 = rajjo(45)

list3.head.next = S2
S2.next = S3
S3.next = S4

sortedlist = LinkedList()

list3 = list3.MergeSorted(list2.head)

list3.printL()