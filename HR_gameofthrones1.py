from sys import stdin
def main():
	word = raw_input() 
	odd = 0
	result = 'YES'
	word_type = len(word)%2
	word_length = len(word)
	while word_length > 0:
		word_counts = word.count(word[0])
		if word_counts%2 == 1 and word_type == 0:
			result = 'NO'
			break
		elif word_counts%2 == 1 and word_type == 1:
			odd+=1
			if odd == 2:
				result = 'NO'
				break
		word = word.translate(None,word[0])
		word_length = len(word)
	print result 



main()
