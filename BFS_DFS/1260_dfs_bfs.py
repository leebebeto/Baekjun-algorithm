from collections import defaultdict
n, m, v = map(int, input().split())
adj_list = defaultdict(list)
visited_list, stack, queue = [], [], []

for i in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

# DFS
stack.append(v)
while len(stack)>0:
    visited = stack.pop()
    if visited not in visited_list:
        visited_list.append(visited)
        new_nodes = sorted(adj_list[visited], reverse=True)
        stack += new_nodes

for visit in visited_list:
    print(visit, end= ' ')

print()
visited_list, stack, queue = [], [], []

# BFS
queue.append(v)
while len(queue) > 0:
    visited = queue.pop(0)
    if visited not in visited_list:
        visited_list.append(visited)
        new_nodes = sorted(adj_list[visited])
        queue += new_nodes
for visit in visited_list:
    print(visit, end= ' ')

print()