def main():
	T = input()
	all_set = []
	for t in range(0,T):
		n = input()
		val1 = input()
		val2 = input()
		set1 = n
		set2 = -1
		res = []
		while set1 > 0:
			set1-=1
			set2+=1
			ans = set1*val1 + set2*val2 
			if ans not in res :
				res.append(ans)
		for i in range(1,len(res)):
			key = res[i]
			j = i -1
			while j>=0 and res[j] > key:
				res[j+1] = res[j]
				j = j - 1
			res[j+1] = key
		all_set.append(res) 
	for a in all_set:
		for b in a:
			print b, 
		print 

main()
