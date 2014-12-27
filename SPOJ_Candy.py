def main():
	bingo = True
	out = []
	while bingo:
		tot = 0
		moves = 0
		candy_arr = []
		pac = int(raw_input())
		if pac == -1:break
		for _ in range(pac):
			candy = int(input())
			candy_arr.append(candy)
			tot+=candy
		if tot%pac == 0:
			_min = tot/pac
			for i in candy_arr:
				if i <= _min:
					moves+= _min-i
			out.append(moves)
		else:
			out.append(-1)	
	for i in out:
		print i
main()
