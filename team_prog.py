#!/usr/bin/python3
import sys 
import pkg_modules 

'''
    Branch 구조
    1. b2h_br - 허진수 담당
    2. fibo_br - 김현지 담당
    3. main_br - 카드리딘 담당
    4. set_br - 이연수 담당
'''

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
