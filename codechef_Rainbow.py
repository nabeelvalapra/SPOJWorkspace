def main():
	x = int(input())
	counter = 0
	if x < 13:
		print 0
	elif x == 13:
		print 1
	elif x > 13:
		extra = (x-13)/2 if (x-13)/2 else 0
		counter =  (7*extra)
		print counter

main()
