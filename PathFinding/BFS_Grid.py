number_row = 5
number_column = 5
matrix = [
    ["Start", "#",  "",  "",   "#"],
    [     "",  "",  "",  "",   "#"],
    [    "#",  "",  "#", "",    ""],
    [     "",  "",  "#", "",   "#"],
    [    "#",  "",  "#", "", "End"]
]

#covart string to int
start_row = None
start_column = None
end_row = None
end_column = None
for row in range(number_row):
    for column in range(number_column):
        if matrix[row][column] == "Start":
            start_row, start_column = row, column
        elif matrix[row][column] == "End":
            end_row, end_column = row, column

#empty queue
queue_row = []
queue_column = []

move_count = 0
node_left_in_layer = 1
node_in_next_layer = 0

reached_end = False

visited = [[False for _ in range(number_column)] for _ in range(number_row)]

direct_row = [-1, +1, 0, 0] #north, south, east, west
direct_column = [0, 0, +1, -1]

def solve():
    global move_count, node_left_in_layer, node_in_next_layer, reached_end
    #enqueue
    queue_row.append(start_row)
    queue_column.append(start_column)
    visited[start_row][start_column] = True
    while len(queue_row) > 0: #queue row size
        #dequeue
        row = queue_row.pop()
        column = queue_column.pop()
        #check reached endpoint
        if matrix[row][column] == "End":
            reached_end = True
            break
        explore_neighbours(row, column)
        #move to left node, move count +1
        node_left_in_layer -= 1
        if node_left_in_layer == 0:
            node_left_in_layer = node_in_next_layer
            node_in_next_layer = 0
            move_count += 1
        print(f"move count: {move_count} -> [{row},{column}]")
    #reached endpoint, return move count value
    if reached_end:
        return move_count
    #not found path
    return -1

def explore_neighbours(row, column):
    global node_in_next_layer

    for i in range(4):
        new_row = row + direct_row[i]
        new_column = column + direct_column[i]

        #check out of bounds
        if new_row < 0 or new_column < 0:
            continue
        if new_row >= number_row or new_column >= number_column:
            continue

        if visited[new_row][new_column]: #check visited
            continue
        if matrix[new_row][new_column] == "#": #check obstacle
            continue

        #mark visited
        queue_row.append(new_row)
        queue_column.append(new_column)
        visited[new_row][new_column] = True
        node_in_next_layer += 1

solve()