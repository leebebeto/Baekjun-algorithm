from collections import defaultdict
node_len = int(input())
link_len = int(input())

adj_list = defaultdict(list)
for i in range(link_len):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

# solving with bfs
queue, visited_list = [], []
node_list = sorted(list(adj_list.keys()))

queue.append(node_list[0])
while len(queue) > 0:
    visited = queue.pop(0)

    if visited not in visited_list:
        visited_list.append(visited)

        # add neighbors in the queue
        neighbors = adj_list[visited]
        queue += neighbors

print(len(visited_list)-1)

# solving with dfs
stack, visited_list = [], []
node_list = sorted(list(adj_list.keys()))
stack.append(node_list[0])

while len(stack) >0:
    visited = stack.pop()

    if visited not in visited_list:
        visited_list.append(visited)
        neighbors = adj_list[visited]
        stack += neighbors

print(len(visited_list)-1)
