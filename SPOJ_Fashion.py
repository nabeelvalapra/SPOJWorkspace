def main():
	out = []
	for _ in range(int(raw_input())):
		mem = int(input())
		men_arr = _sort(raw_input().rstrip().split())
		women_arr = _sort(raw_input().rstrip().split())
		tot_arr = [int(men_arr[x])*int(women_arr[x]) for x in range(mem)]
		tot = 0
		for i in tot_arr:
			tot+=i
		out.append(tot)
	for i in out:
		print i

def _sort(arr):
	out = []
	ct_arr = [0]*11
	j = 0
	for i in arr:
		ct_arr[int(i)]+=1
	while j < 11:
		if ct_arr[j] > 0:
			out.extend([j]*ct_arr[j])
		j+=1
	return out

main()
