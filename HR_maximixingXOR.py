from math import floor
def main():
	a = int(input())
	b = int(input())
	
	bin_a,bin_b = binary(a),binary(b)	
	res_xor =  str(xor(bin_a,bin_b))
	power = out =0
	for i in range(0,len(res_xor)):
		out += int(res_xor[i])*pow(2,i)
	print out
		

def binary(num):
	out = ''
	if num == 0:
		out = '0'
	while num>0:
		if num%2==0:
			out = str('0') + out
			num = num/2
		else:
			out = str('1') + out
			num = int(floor(num/2))
	return out

def xor(num1,num2):
	len_num1 = len(num1)
	len_num2 = len(num2)
	length = len_num1 if len_num1>=len_num2 else len_num2
	res = str()
	c = 0
	while len(num1) > len(num2):
		num2=str('0')+num2
	while len(num2) > len(num1):
		num1=str('0')+num1
	while c < length:
		if (num1[c] == '0' and num2[c] == '0') or (num2[c] == '1' and num1[c] == '1'):
			res = '0' + res
		else:
			res = '1' + res
		c+=1	
	return int(res)
	
main()
