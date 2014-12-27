from sys import stdin
def main(): 
	num_word = int(raw_input())
	words = [stdin.readline().rstrip() for i in range(0,num_word)] 
	hole = ['A','Q','D','O','P','R','B']
	out = []
	for word in words:
		counter = 0
		for letter in range(len(word)):
			if word[letter] in hole:
				counter +=1
			if word[letter] == 'B':
				counter +=1
		out.append(counter)
 	for i in out:
		print i

main()

