m = int(input())

flag_answer = False
for i in range(m):
    summed = i
    each_m_list = list(str(i))
    for each_m in each_m_list:
        summed += int(each_m)
    if summed == m:
        print(i)
        flag_answer = True
        break

if flag_answer == False:
    print(0)