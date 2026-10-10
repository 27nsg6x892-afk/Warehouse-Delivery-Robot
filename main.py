from collections import deque
from time import perf_counter
import heapq
from itertools import count

# Define the Maps

MAP_A = [
    "S..#....",
    "##.#.##.",
    "....~~..",
    ".####.#.",
    "...~..#G"
]

MAP_B = [
    "S~~~~~~~G",
    ".#######.",
    ".........",
    ".#.#.#.#.",
    "........."
]

MAP_C = [
    "S..#....",
    ".#.#.##.",
    "...#..#.",
    ".###.##.",
    "....#..G"
]
map_name = "MAP_A"  
# Select the map
GRID = MAP_A  # Change to MAP_B or MAP_C as needed



# Find Start and Goal Positions

def find_positions(grid):
    start = None
    goal = None

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] == 'S':
                start = (row, col)

            elif grid[row][col] == 'G':
                goal = (row, col)

    return start, goal


start, goal = find_positions(GRID)

print("Start:", start)
print("Goal:", goal)

# available moves 

def get_neighbors(grid, position):

    row, col = position

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if (0 <= new_row < len(grid) and
            0 <= new_col < len(grid[new_row]) and
            grid[new_row][new_col] != '#'):

            neighbors.append((new_row, new_col))

    return neighbors


# Cost Function
def get_cost(grid, position):

    row, col = position

    if grid[row][col] == '~':
        return 3

    return 1




def bfs(grid, start, goal):

    queue = deque([start])

    visited = {start}

    parent = {start: None}

    nodes_expanded = 0
    max_frontier_size = 1

    start_time = perf_counter()

    while queue:

        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

        max_frontier_size = max(
            max_frontier_size, len(queue)
        )

    run_time = perf_counter() - start_time

    if goal not in visited:
        return None, 0, nodes_expanded, max_frontier_size, run_time

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    total_cost = sum(
        get_cost(grid, position)
        for position in path[1:]
    )

    return (
        path,
        total_cost,
        nodes_expanded,
        max_frontier_size,
        run_time
    )



def display_path(grid, path):

    map_copy = [list(row) for row in grid]

    if path is None:
        print("No path found")
        return

    for row, col in path[1:-1]:
        map_copy[row][col] = '*'

    for row in map_copy:
        print("".join(row))






# A* Search Implementation

# manhattan distance heuristic function
def manhattan_distance(position, goal):

    row1, col1 = position
    row2, col2 = goal

    return abs(row1 - row2) + abs(col1 - col2)


def a_star(grid, start, goal):

    start_time = perf_counter()

    # Priority Queue
    frontier = []

    # Unique number for tie-breaking
    counter = count()

    # Cost from Start to each node
    g_cost = {start: 0}

    # Store parents to reconstruct path
    parent = {start: None}

    # Calculate initial heuristic
    h = manhattan_distance(start, goal)

    heapq.heappush(
        frontier,
        (h, next(counter), 0, start)
    )

    nodes_expanded = 0
    max_frontier_size = 1

    while frontier:

        f, _, current_g, current = heapq.heappop(
            frontier
        )

        # Skip outdated entries
        if current_g != g_cost[current]:
            continue

        nodes_expanded += 1

        # Goal Test
        if current == goal:
            break

        # Explore neighbors
        for neighbor in get_neighbors(grid, current):

            movement_cost = get_cost(grid, neighbor)

            new_g = g_cost[current] + movement_cost

            if new_g < g_cost.get(
                neighbor, float('inf')
            ):

                g_cost[neighbor] = new_g

                parent[neighbor] = current

                h = manhattan_distance(neighbor, goal)

                f = new_g + h

                heapq.heappush(
                    frontier,
                    (f, next(counter), new_g, neighbor)
                )

        max_frontier_size = max(
            max_frontier_size, len(frontier)
        )

    run_time = perf_counter() - start_time

    # Check if Goal was reached
    if goal not in g_cost:
        return None, 0, nodes_expanded, max_frontier_size, run_time

    # Reconstruct Path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    total_cost = g_cost[goal]

    return (
        path,
        total_cost,
        nodes_expanded,
        max_frontier_size,
        run_time
    )







MAPS = {
    "MAP_A": MAP_A,
    "MAP_B": MAP_B,
    "MAP_C": MAP_C
}


def run_tests():

    results = []

    # Loop through all maps
    for map_name, grid in MAPS.items():

        start, goal = find_positions(grid)

        print(f"\n{'=' * 50}")
        print(f"Testing {map_name}")
        print("=" * 50)

        # Search Algorithms
        algorithms = [
            ("BFS", bfs),
            ("A*", a_star)
        ]

        # Run each algorithm
        for name, algorithm in algorithms:

            path, cost, expanded, frontier, runtime = algorithm(
                grid, start, goal
            )

            print(f"\nAlgorithm: {name}")

            if path is not None:
                length = len(path) - 1

                print("Path:", path)
                print("Path Length:", length)
                print("Total Cost:", cost)

            else:
                length = "N/A"
                cost = "N/A"

                print("No path found")

            print("Nodes Expanded:", expanded)
            print("Maximum Frontier Size:", frontier)
            print(f"Run Time: {runtime:.6f} seconds")

            print("\nPath Visualization:")
            display_path(grid, path)

            # Store results
            results.append({
                "Map": map_name,
                "Algorithm": name,
                "Length": length,
                "Cost": cost,
                "Expanded": expanded,
                "Frontier": frontier,
                "Time": runtime * 1000
            })

    # Final Comparison Table
    print("\n" + "=" * 85)
    print("FINAL COMPARISON TABLE")
    print("=" * 85)

    print(
        f"{'Map':<10}"
        f"{'Algorithm':<12}"
        f"{'Length':<10}"
        f"{'Cost':<10}"
        f"{'Expanded':<12}"
        f"{'Frontier':<12}"
        f"{'Time(ms)':<12}"
    )

    print("-" * 85)

    for result in results:

        print(
            f"{result['Map']:<10}"
            f"{result['Algorithm']:<12}"
            f"{str(result['Length']):<10}"
            f"{str(result['Cost']):<10}"
            f"{result['Expanded']:<12}"
            f"{result['Frontier']:<12}"
            f"{result['Time']:<12.4f}"
        )

    return results


if __name__ == "__main__":
    run_tests()
