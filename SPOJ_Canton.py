def main():
	for _ in range(int(raw_input())):
		counter, i = 0, 0
		num = int(input())
		while counter < num:
			counter += i+1 
			i += 1
		upper, lower = counter, counter-i+1
		i -= 1
		counter -= i		
		a = 1
		b = i+1 if num != 1 else 1
		if not counter == lower or not counter == upper:
			while counter < num:
				counter += 1
				a += 1
				b -= 1
		if i%2:
			print 'TERM '+str(num)+' IS '+ str(a) +'/'+ str(b) 
		else:
			print 'TERM '+str(num)+' IS '+ str(b) +'/'+ str(a)
main()
