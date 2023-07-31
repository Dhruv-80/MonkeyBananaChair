from queue import Queue

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def bfs_shortest_path(grid, start_pos, target_pos):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = Queue()
    parent = {}  

    queue.put((start_pos, 0))  # Tuple format: ((x, y), steps)
    visited[start_pos[0]][start_pos[1]] = True

    while not queue.empty():
        (x, y), steps = queue.get()

        # Check if we have reached the target position
        if (x, y) == target_pos:
            # Reconstruct the path and return it
            path = []
            current_pos = target_pos
            while current_pos != start_pos:
                path.append(current_pos)
                current_pos = parent[current_pos]
            path.append(start_pos)
            path.reverse()
            return steps, path

        # Check and add valid neighbors to the queue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols) and not visited[new_x][new_y] and grid[new_x][new_y] != '#':
                visited[new_x][new_y] = True
                parent[(new_x, new_y)] = (x, y)
                queue.put(((new_x, new_y), steps + 1))

    # If the target position is unreachable
    return -1, []

if __name__ == "__main__":
    grid = [
        ['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3']
    ]

    banana_pos_input = input("Enter the position of the banana (e.g., A2): ")
    chair_pos_input = input("Enter the position of the chair (e.g., C3): ")
    monkey_pos_input = input("Enter the position of the monkey (e.g., B1): ")

    banana_pos = (ord(banana_pos_input[0]) - ord('A'), int(banana_pos_input[1]) - 1)
    chair_pos = (ord(chair_pos_input[0]) - ord('A'), int(chair_pos_input[1]) - 1)
    monkey_pos = (ord(monkey_pos_input[0]) - ord('A'), int(monkey_pos_input[1]) - 1)

    # Find the shortest path from monkey to banana
    banana_steps, banana_path = bfs_shortest_path(grid, chair_pos, banana_pos)
  
    # Find the shortest path from monkey to chair
    chair_steps, chair_path = bfs_shortest_path(grid, monkey_pos, chair_pos)

    if chair_steps != -1:
        print(f"Shortest distance to the chair: {chair_steps} steps")
        print("Steps taken:")
        for position in chair_path:
            print(grid[position[0]][position[1]], end=" -> ")
        print("Chair")
    else:
        print("The chair is unreachable from the monkey's position.")

    if banana_steps != -1:
        print(f"Shortest distance to the banana: {banana_steps} steps")
        print("Steps taken:")
        for position in banana_path:
            print(grid[position[0]][position[1]], end=" -> ")
        print("Banana")
    else:
        print("The banana is unreachable from the monkey's position.")
