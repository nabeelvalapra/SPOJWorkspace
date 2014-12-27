from sys import stdin
def main():
	T = input()
	if T > 0 :
		first_element = stdin.readline().rstrip()
		first_element = list(first_element)
	else:
		return 0
	counter = 1
	gem_letters = first_element
	new_gem_letters = []
	while counter < T:
		next_element = list(stdin.readline().rstrip())
		for i in next_element:
			if i in gem_letters:
				new_gem_letters.append(i)
		gem_letters = new_gem_letters
		new_gem_letters = [] 
		counter+=1
	print len(set(gem_letters))
main()
