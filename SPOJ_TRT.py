import sys
import gc
gc.disable()

def main():
	lst = []
	tot = 0
	t = int(sys.stdin.readline().rstrip())
	for _ in range(t):
		lst.append(int(sys.stdin.readline().rstrip()))
	print dp(lst,1)



def dp(arr,day):
	if len(arr) <= 1:
		return arr[0]*day
	else:
		return  max((arr[0]*day)+dp(arr[1:],day+1), (arr[-1]*day)+dp(arr[:-1],day+1))
		
main()
