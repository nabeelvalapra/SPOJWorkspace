def main():
	cash, init_bal =  map(float,raw_input().split())
	try :
		cash = float(cash)
		init_bal = float(init_bal)
	except :
		exit()

	if cash % 5 != 0 or cash > init_bal or cash > (init_bal - 0.50):
		print "%0.2f"%init_bal
	else: 
		bal = (init_bal - cash) - 0.50
		print "%0.2f"%bal
main()
