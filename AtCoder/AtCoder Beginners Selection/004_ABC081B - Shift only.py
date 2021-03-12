length = int(input())

num_list = []

count = 0
ans_count = 0

num_list = list(map(int,input().split()))

while True:
    for i in num_list:
        if i%2 == 0:
            count += 1

    num_list = [x / 2 for x in num_list]
    
    if count == length:
        count = 0
        ans_count += 1
    else:
        break

print(ans_count)

