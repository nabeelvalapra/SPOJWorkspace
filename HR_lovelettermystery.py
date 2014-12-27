from sys import stdin
def main():
	T = int(input())
	results = []
	for a in range(0,T):
		word = stdin.readline().rstrip()
		results.append(moves(word))
	
	for i in results:
		print i

def moves(word):
	mid = len(word)/2	
	counter = 0
	index = 0
	backindex = len(word)-1
	while index < mid:
		if word[backindex] > word[index] :
			counter += int(ord(word[backindex]))-int(ord(word[index]))
		else:
			counter += int(ord(word[index]))-int(ord(word[backindex]))
		index+=1
		backindex-=1

	return counter
main()

