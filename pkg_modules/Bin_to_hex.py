def Bin_to_hex(binary):
    integer = int(binary,2)
    print(f'hexa number: {hex(integer)}')

if __name__=="__main__":
    binary = input("input bin number: ")
    Bin_to_hex(binary)