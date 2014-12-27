def main():
	print fact(8735373)
	print ctzero(fact(60))
def ctzero(num):
	for a in range(len(str(num)),0):
		if num[a] == str(num):
			print num[a]
			
def fact(a):return a*fact(a-1) if a > 0 else 1
main()
