from sys import stdin
def main():
	T = int(raw_input())
	result = []
	if T == 0:
		result.append("NO")
	for i in range(0,T):
		
		array = []
		flag = 1
		result.append('NO')
		temp_result = 0

		n,k = map(int,stdin.readline().split())
		array.extend(stdin.readline().rstrip())
		[array.pop(array.index(x)) for x in array if x==' ']

		if len(array) > n:
			flag = 0
		if len(array) != len(set(array)):
			flag = 0
		
		for emnt in array:
			if ((int(emnt)%2 == 0 or k == 0) and int(emnt)!=0) and flag == 1:
				temp_result+=1 
				if temp_result >= k or k == 0:
					result[i] = "YES"
 				else: 
					result[i] = "NO"
			else:
				temp_result = 0
	for i in result:
		print i		

main()
