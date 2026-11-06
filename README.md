# Island Counter

**Category:** Graph Algorithms  
**Language:** Python 3 (standard library only)

## Idea
A map contains 1 (land) and 0 (water). Adjacent land cells belong to one island. We use **Breadth-First Search (BFS)** to count the number of connected groups of land.

## Steps
1. Scan the grid cell by cell.
2. When an unvisited land cell is found, start a BFS.
3. Visit all connected land cells in the four directions: up, down, left, and right.
4. Increase the island count once per BFS.

Diagonal cells do **not** connect. The original map is not changed.

## Run
```bash
python main.py
python main.py sample_map.txt
python -m unittest -v
```

Grid input file: one row per line, only `0` and `1`, with equal row lengths.

## Complexity
For R rows and C columns: **O(R × C)** time, **O(R × C)** space worst case for the visited set and queue.
