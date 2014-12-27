def main():
	for _ in range(int(raw_input())):
		H = raw_input()
		counter = 0
		if palin(H):
			counter+=1
		else:
			counter = 2
		print counter
def palin(H):
	revH = H[::-1]
	if revH == H:
		return True
	else:
		return False

main()
