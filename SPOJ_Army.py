from sys import stdin
import gc
gc.disable()
def main():
	for _ in range(int(stdin.readline())):
		stdin.readline()
		stdin.readline()
		a = max(map(int,stdin.readline().split()))
		b = max(map(int,stdin.readline().split()))
		if a < b :
			print 'MechaGodzilla'			
		else:
			print 'Godzilla'
	print 
main()
