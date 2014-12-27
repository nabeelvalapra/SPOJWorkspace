def main():
	out = []
	T = int(raw_input())
	for i in range(T):
		x, y = map(int,raw_input().split())
		assert 1 <= x <= y <= 1000000000
		assert y-x <= 100000
		lst = get_primes(x,y)
		if i < T-1:
			lst.append('\n')
		out.append(lst)

	for _ in out:
		for __ in _:
			print __


def get_primes(low,n):
	if n == 2 :return [2]
	elif n <= 0 :return []
	m = low if low > 2 else 2
	i = 0
	odd_set = range(low,n+1,2)
	half = n/2 + 1
	root = n**0.5
	while m <= root:
		if odd_set != 0:
			j = ((m*m)-3)/2 if (m*m)-3 != 0 else 0
			if j <= half:
				odd_set[j] = 0
				j = j+m
		i = i+1
		m = (2*i)+1
	if_two = []
	if low<2:
		if_two = [2]	
	return if_two + [x for x in odd_set if x != 0 and x >= low]

main()
