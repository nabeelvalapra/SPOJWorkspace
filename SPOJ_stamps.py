def main():
	for case in range(int(raw_input())):
		_max, m = map(int,raw_input().rstrip().split())		
		arr = map(int,raw_input().rstrip().split())
		arr.sort()
		total, ct = 0, 0
		bingo = False
		for i in range(len(arr)-1,-1,-1):
			total += arr[i]
			ct +=1
			if total >= _max:
				bingo = True	
				break
		if bingo == True:
			print "Scenario #"+str(case+1)+":"
			print ct
		else:
			print "Scenario #"+str(case+1)+":"
			print "impossible"
		print 
main()
