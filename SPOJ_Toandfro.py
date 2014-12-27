def main():
	out = []
	while True:	
		col = input()
		if col == 0:break
		cipher = raw_input()
		table = []
		ct, i = 0, 0
		while len(cipher) >= i+col:
			row = cipher[i:i+col] if ct%2 == 0 else cipher[i:i+col][::-1]
			table.append(list(row))
			i+=col
			ct+=1
		ct = 0	
		text = []
		while ct < col:
			for _row in table:
				text.append(_row[ct])
			ct+=1
		out.append(text)
	for a in out:
		print ''.join(a)				
main()
