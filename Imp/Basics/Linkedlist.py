class Node:
	def __init__(self, key=None, next=None):
		self.key = key
		self.next = next
	
	def __str__(self):
		return str(self.key)

class Linkedlist:
	def __init__(self):
		self.first_node = None 
		self.last_node =  None
	
	def append(self, new_key):
		if self.first_node == None:
			self.first_node = Node(new_key,None)
			self.last_node = self.first
		else:
			new_node = Node(new_key, None)
			self.last_node.next = new_node
			#Here we append 'New_node' to the 'Last_node' using 'next' keyword,
			#but still the 'Last_node' is '(Last_node-1)th node' now.
			self.last_node = new_node
			#Here we declare the 'Last_Node' as the 'node' we added above.
		
	def __str__(self):
		if self.first != None:
			node = self.first
			out = 'LinkedList::[' + str(node.key)
			while node.next != None:
				out += ','
				node = node.next
				out += str(node.key) 
			return out + ']'
		return 'LinkedList []'
	
	
