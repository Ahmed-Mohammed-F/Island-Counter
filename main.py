"""Count islands in a 0/1 map using BFS (four directions)."""
from collections import deque
from pathlib import Path
import sys

SAMPLE = Path(__file__).resolve().parent / "sample_map.txt"


def read_grid(filename):
    lines = Path(filename).read_text(encoding="utf-8").splitlines()
    grid = [list(line.replace(" ", "").strip()) for line in lines if line.strip()]
    if not grid or any(len(row) != len(grid[0]) for row in grid):
        raise ValueError("The map must be a non-empty rectangular grid")
    if any(cell not in ("0", "1") for row in grid for cell in row):
        raise ValueError("Use only 0 for water and 1 for land")
    return grid


def count_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    if any(len(row) != cols for row in grid):
        raise ValueError("Rows must have equal lengths")
    seen = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            queue = deque([(r, c)])
            seen.add((r, c))
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and
                        grid[nx][ny] == "1" and (nx, ny) not in seen):
                        seen.add((nx, ny))
                        queue.append((nx, ny))
    return islands


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else SAMPLE
    grid = read_grid(filename)
    print("Map (1 = land, 0 = water):")
    for row in grid:
        print("".join(row))
    print("Number of islands:", count_islands(grid))
