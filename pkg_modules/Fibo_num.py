#!/usr/bin/python

def Fibo_num():
    n = int(input("fibonacci number: "))
    curr, next = 0, 1
    for _ in range(n):
        curr, next = next, curr + next
        print(curr, end=" ")
    print("\nF{0} = {1}".format(n, curr))

if __name__=="__main__":
    Fibo_num()
