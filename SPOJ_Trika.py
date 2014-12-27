from sys import stdin
def main():
	n, m = map(int,stdin.readline().rstrip().split())
	x, y = map(int,stdin.readline().rstrip().split())
	arr = []
	for r in range(n):
		row = map(int,stdin.readline().rstrip().split())
		arr.append(row)
	i, j = 1, 0	
	while i	<= n-1:
		arr[i][j] = arr[i-1][j] - arr[i][j]
		i+=1
	i, j = 0, 1
	while j <= m-1:
		arr[i][j] = arr[i][j-1] - arr[i][j]
		j+=1
	i = 1
	while i <= n-1:
		j = 1	
		while j <= m-1:
			arr[i][j] = max(arr[i-1][j],arr[i][j-1]) - arr[i][j]
			j+=1
		i+=1
	if arr[i-1][j-1]<0:print 'N'
	else:
		 print 'Y ' + str(arr[i-1][j-1]) 
main()
