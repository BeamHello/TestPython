from collections import deque

number_row = 4
number_column = 4
matrix_size = [["Emtpy" for _ in range(number_column)] for _ in range(number_row)]
matrix_size[3][3] = "End" # Set end point

start_row = 0
start_column = 0

queue_row = deque()
queue_column = deque()

move_count = 0
node_left_in_layer = 1
node_in_next_layer = 0

reached_end = [False]

visited = [[False for _ in range(number_column)] for _ in range(number_row)]

direct_row = [-1, 1, 0, 0]
direct_column = [0, 0, 1, -1]

def solve():
    global move_count, node_left_in_layer, node_in_next_layer, reached_end

    queue_row.append(start_row)
    queue_column.append(start_column)
    visited[start_row][start_column] = True
    while queue_row:
        row = queue_row.popleft()
        column = queue_column.popleft()

        # Check reached endpoint
        if matrix_size[row][column] == "End":
            reached_end = True
            break

        explore_neighbours(row, column)

        node_left_in_layer -= 1
        if node_left_in_layer == 0:
            node_left_in_layer = node_in_next_layer
            node_in_next_layer = 0
            move_count += 1
        if reached_end:
            return move_count
        
    # no found path
    return -1

def explore_neighbours(row, column):
    global node_in_next_layer

    for i in range(4):
        new_row = row + direct_row[i]
        new_column = column + direct_column[i]

        # Check boundaries
        if new_row < 0 or new_column < 0:
            continue
        if new_row >= number_row or new_column >= number_column:
            continue

        if visited[new_row][new_column]: # Check visited
            continue
        if matrix_size[new_row][new_column] == "#": # Check obstacle
            continue

        # mark visited
        queue_row.append(new_row)
        queue_column.append(new_column)
        visited[new_row][new_column] = True
        node_in_next_layer += 1

result = solve()
print("Minimum moves to reach the end:" if result != -1 else "End not reachable", result)