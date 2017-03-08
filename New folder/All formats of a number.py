# Read the integer, and print the decimal, octal, hexadecimal, and binary values from to with space padding so that all fields
# take the same width as the binary value.
n=int(input('Enter a number : '))
# 2: in bin because a number say 10 = 0b1010
width=len(bin(n)[2:])
print('DECIMAL'.rjust(width,' '),'OCTAL'.rjust(width,' '),'HEXADECIMAL'.rjust(width,' '),'BINARY'.rjust(width,' '))
for i in range(1,n+1):
    print(str(i).center(width,' '),str(oct(i)[2:]).center(3*width,' '),str(hex(i)[2:].upper()).center(width,' '),str(bin(i)[2:]).center(3*width,' '))