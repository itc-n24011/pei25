a = 0b11010
b = 0b10100
c = a & b
d = a | b
c >>= 2
e = d - c
print(f'{e:b}')

