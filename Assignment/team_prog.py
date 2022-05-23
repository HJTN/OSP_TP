#!/usr/bin/python3
import sys 
import pkg_modules 


def get_selected_menu(n):
	if n == 1: #run bin-to-hex function from pkg_modules 
		pkg_modules.Bin_to_hex() 
	elif n == 2: #run un/intersec function from pkg_modules 
		pkg_modules.uni_inter_set() 
	elif n == 3: #run fib_num function from pkg_modules 
		pkg_modules.Fibo_num()
	elif n == 4: #exit program with "exit the program..." message 
		sys.exit("exit the program...")
	else:
		print("Invalid input! Choose integer from 1 to 4\n") 

 
if __name__=='__main__':
	while True: 
		menu = int(input("Select menu: 1)b2h 2)set 3)fibo 4)exit ?"))
		get_selected_menu(menu)
		print() 
