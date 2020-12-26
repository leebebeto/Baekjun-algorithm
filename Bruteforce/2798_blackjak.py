m,n = map(int, input().split())

num_list = list(map(int, input().split()))

answer = 0
sum_set = set()
triple2sum = {}
index=0

for i in range(m):
    for j in range(i+1, m):
        for k in range(j + 1, m):
            triplet= (num_list[i], num_list[j], num_list[k])
            sum_set.add(triplet)

for item in sum_set:
    temp_sum = item[0] + item[1] + item[2]
    triple2sum[item] = temp_sum

triple2sum = sorted(triple2sum.items(), key=lambda x : x[1], reverse=True)

flag_answer = False
for sum in triple2sum:
    k, v = sum[0], sum[1]
    if sum[1] <= n:
        answer = k[0] + k[1] + k[2]
        print(answer)
        break