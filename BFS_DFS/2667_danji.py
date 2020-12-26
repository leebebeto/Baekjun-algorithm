from collections import defaultdict
import sys
n = int(input())
lines = []
for i in range(n):
    line = list(map(int, input()))
    lines.append(line)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# array list -> copied array list with padding 1
array_list, visited_list, answer_list = [], [], []

for i in range(n+2):
    temp_array = [0 for i in range(n+2)]
    temp_visit = [False for i in range(n+2)]

    array_list.append(temp_array)
    visited_list.append(temp_visit)

for row, line in enumerate(lines):
    for col, item in enumerate(line):
        if item == '\n':
            break
        array_list[row+1][col+1] = int(item)


def bfs(x, y):
    queue.append((x, y))
    each_cnt = 0
    while len(queue) > 0:
        each_cnt += 1
        node = queue.pop(0)
        x, y = node[0], node[1]
        for i in range(4):
            if array_list[x+dx[i]][y+dy[i]] == 1 and visited_list[x+dx[i]][y+dy[i]] == False:
                neighbor = array_list[x+dx[i]][y+dy[i]]
                visited_list[x + dx[i]][y + dy[i]] = True
                queue.append((x + dx[i], y + dy[i]))
    return each_cnt

answer, queue, each_cnt_list = 0, [], []
for x in range(1, n+1):
    for y in range(1, n+1):
        if array_list[x][y] == 1 and visited_list[x][y] == False:
            visited_list[x][y] = True
            each_cnt = bfs(x, y)
            each_cnt_list.append(each_cnt)
            answer += 1

print(answer)
each_cnt_list = sorted(each_cnt_list)
for each_cnt in each_cnt_list:
    print(each_cnt)
