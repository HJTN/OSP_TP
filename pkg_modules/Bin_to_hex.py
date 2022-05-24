def Bin_to_hex():
    binary = input("input bin number: ")
    integer = int(binary,2)
    print(f'hexa number: {hex(integer)}')

if __name__=="__main__":
    Bin_to_hex()