#Singly Linkedlist
class Linkedlist:
	#A Node contains a 'key' and 'next'(as pointer),
	#Remember 'next' is a keyword
	class Node:
		def __init__(self, key=None, next=None):
			self.key = key
			self.next = next
		
		def __str__(self):
			return str(self.key)
	
	def __init__(self):
		#We create TWO nodes(variables), the first_node and last_node
		#In case a first element comes we assign it to the 'first_node' and
		# make THIS node as the 'last_node'.(Check the append method for more).
		self.first_node = None
		self.last_node = None
	
	#'prepend' adds a 'Node' to the first of the LinkedList object.
	def prepend(self, new_key):
		new_node = self.Node(new_key,None)
		if self.first_node == None:
			self.first_node = new_node
			self.last_node = self.first_node
		else:
			new_node.next = self.first_node
			self.first_node = new_node		
	
	#'append' adds a 'Node' to the last of the LinkedList object.
	def append(self, new_key):
		new_node = self.Node(new_key,None)
		if self.first_node == None:
			self.first_node = new_node
			self.last_node = self.first_node
		else:
			self.last_node.next = new_node
			self.last_node = new_node
	
	#'search' returns 'true' if element is present in the list, else 'false'
	def search(self, key):
		in_list = False
		if self.first_node != None:
			node = self.first_node
			while node.next != None:
				if node.key == key:	
					in_list = True
					break
				else:
					node = node.next	
		return in_list
			
	#Return the number of elements
	def count(self):
		counter = 0
		if self.first_node != None:
			node = self.first_node
			counter = 1
			while node.next != None:
				counter+=1
				node = node.next
		return counter

	#Print the list with {}
	def __str__(self):
		if self.first_node != None:
			node = self.first_node
			out = '{'+str(node.key)
			while node.next != None:
				out+=','
				node = node.next
				out+=str(node.key)
			return out+'}'
		return '{}'	

















