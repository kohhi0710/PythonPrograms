#初カキコ…ども…

A = int(input())
B = int(input())
C = int(input())
X = int(input())

a_values = [i for i in list(range(500,(500 * A) + 1, 500)) if i <= X]
b_values = [i for i in list(range(100,(100 * B) + 1, 100)) if i <= X]
c_values = [i for i in list(range(50,(50 * C) + 1, 50)) if i <= X]

#append 単一の要素をリストの末尾に付加する
a_values.append(0)
b_values.append(0)
c_values.append(0)

z = 0

for ia in a_values:
    for ib in b_values:
        for ic in c_values:

            if ia + ib + ic == X:
                z += 1

print(z)