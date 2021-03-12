from itertools import product

items = ["A", "B", "C", "D", "E", "F"]
A = [0, 1]
B = [0, 1]
C = [0, 1]
D = [0, 1]
E = [0, 1]
F = [0, 1]

for bits in product(A,B,C,D,E,F):
    comb = [x for bit in zip(items,bits) if bit == 1]
    print(comb)
