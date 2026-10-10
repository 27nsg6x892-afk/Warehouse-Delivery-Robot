# Warehouse Delivery Robot

## Intelligent Systems - Task 1

This project implements and compares two search algorithms,
Breadth-First Search (BFS) and A\* Search, for warehouse
robot navigation.

## Problem Description

A robot must navigate from a start position (S) to a
goal position (G) in a warehouse grid.

The robot can move Up, Down, Left, or Right.

### Grid Symbols

| Symbol | Description  | Cost            |
| ------ | ------------ | --------------- |
| S      | Start        | 0 initially     |
| G      | Goal         | 1               |
| .      | Normal Floor | 1               |
| ~      | Rough Floor  | 3               |
| #      | Wall         | Not traversable |

## Implemented Algorithms

### Breadth-First Search (BFS)

- Uninformed search algorithm.
- Uses a FIFO Queue.
- Finds the shortest path in terms of steps.
- Does not guarantee the lowest path cost.

### A\* Search

- Informed search algorithm.
- Uses a Priority Queue.
- Uses Manhattan Distance as a heuristic.
- Finds the minimum-cost path.

## How to Run

Requirements:

- Python 3
- No external libraries required

Run the program:

```bash
python main.py
```

The program automatically tests BFS and A\* on
MAP_A, MAP_B, and MAP_C.

## Changing the Map

The maps are defined at the beginning of main.py.

To change the map for individual algorithm tests:

```python
GRID = MAP_B
```

The run_tests() function tests all three maps
regardless of the selected GRID variable.

## Results

| Map   | Algorithm | Length | Cost | Expanded | Frontier |
| ----- | --------- | ------ | ---- | -------- | -------- |
| MAP_A | BFS       | 11     | 15   | 28       | 5        |
| MAP_A | A\*       | 11     | 15   | 21       | 5        |
| MAP_B | BFS       | 8      | 22   | 25       | 4        |
| MAP_B | A\*       | 12     | 12   | 15       | 7        |
| MAP_C | BFS       | N/A    | N/A  | 13       | 3        |
| MAP_C | A\*       | N/A    | N/A  | 13       | 3        |

## Conclusion

A\* is more suitable for this warehouse robot because
it considers movement costs and finds cheaper paths
when different terrain costs are present.

## Project Files

- main.py: Python implementation.
- screenshots/: Algorithm outputs and comparison table.
- report.pdf: Detailed project report.
