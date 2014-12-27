def main():
	n = int(raw_input())
	i = 1
	temp = n/i - i + 1
	tot = 0
	while temp >= 0:
		i += 1
		tot += temp
		temp = n/i - i + 1
	print tot 	
main()
