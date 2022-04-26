#!/usr/bin/python

def Fibo_num(n):
    curr, next = 0, 1
    for _ in range(n):
        curr, next = next, curr + next
        print(curr, end=" ")
    print("\nF{0} = {1}".format(n, curr))

if __name__=="__main__":
    n = int(input("fibonacci number: "))
    Fibo_num(n)
