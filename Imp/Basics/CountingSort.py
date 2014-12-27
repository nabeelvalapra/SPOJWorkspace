from sys import stdin
def main():
	T = input()
	nums = map(int,stdin.readline().rstrip().split())
	final_array = [0 for i in range(0,100)]
	assert len(nums) == T
	for x in nums:
		if x in range(0,100):
			final_array[x]+=1
	for i in final_array:
		print i,
main()
