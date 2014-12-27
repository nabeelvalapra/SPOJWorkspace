from sys import stdin
def main():
	T = input()
	arr = [list(stdin.readline().rstrip()) for x in range(0,T)]
	last_index = int(T -1)
	for i in range(1,last_index):
		for j in range(1,last_index):
			index_is_greatest = True
			adj_arr = [arr[i-1][j],arr[i+1][j],arr[i][j-1],arr[i][j+1]]
			if 'X' in adj_arr:
				index_is_greatest = False
			for x in adj_arr:
				if arr[i][j] <= x:
					index_is_greatest = False
			if index_is_greatest:
				arr[i][j] = 'X'
	for i in range(T):
		row = []
		for j in range(T):
			row.append(arr[i][j])
		print ''.join(map(str,row))
main()
