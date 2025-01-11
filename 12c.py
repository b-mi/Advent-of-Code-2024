#Advent of Code 2024: Day 12
from collections import defaultdict, deque
from datetime import datetime
time_start = datetime.now()

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_grid(lines):
    grid = defaultdict(list)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grid[char].append((r,c))
    return grid, len(lines), len(lines[0])

def find_region_size_and_perimeter(coords):
    directions = [(-1, 0), (1,0), (0,-1), (0,1)] #UDlR
    queue = deque([coords[0]])
    visited = [coords[0]]
    while queue:
        current = queue.popleft()
        neighbours = [tuple_sum(direction, current) for direction in directions]
        for neighbour in neighbours:
            if neighbour in coords and neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    perimeter = 0
    for coord in visited:
        neighbours = [tuple_sum(direction, coord) for direction in directions]
        neighbours = [neighbour for neighbour in neighbours if neighbour in visited]
        perimeter += 4 - len(neighbours)
    return visited, perimeter

def scan_rows(start, finish, step, region):
    sides = 0
    used_cols = []
    for i in range(start, finish, step): #check cols from top to bottom ev. bottom to top
        row = list(filter(lambda coord: coord[0]==i, region)) #get all coords on i-th row
        _, cols = zip(*row) #get all column coords in i-th row
        groups = []
        for num in sorted(cols):
            if not groups or num - groups[-1][-1] > 1: #if group is empty or differs by more than one
                if num not in used_cols:
                    used_cols.append(num)
                    groups.append([num])
            else:
                if num not in used_cols:
                    used_cols.append(num)
                    groups[-1].append(num)
        used_cols = [col for col in cols]
        sides += len(groups)
    return sides

def scan_cols(start, finish, step, region):
    sides = 0
    used_rows = []
    for i in range(start, finish, step): #check cols from left to right ev. right to left
        col = list(filter(lambda coord: coord[1]==i, region)) #get all coords on i-th col
        rows, _ = zip(*col) #get all row coords in i-th row
        groups = []
        for num in sorted(rows):
            if not groups or num - groups[-1][-1] > 1: #if group is empty or differs by more than one
                if num not in used_rows:
                    used_rows.append(num)
                    groups.append([num])
            else:
                if num not in used_rows:
                    used_rows.append(num)
                    groups[-1].append(num)
        used_rows = [col for col in rows]
        sides += len(groups)
    return sides

def count_sides(region):
    r_s, c_s = zip(*region)
    min_r, max_r = min(r_s), max(r_s) #define borders of region
    min_c, max_c = min(c_s), max(c_s)
    sides = 0
    sides += scan_rows(min_r, max_r+1, 1, region) #scan from top to bottom
    sides += scan_rows(max_r, min_r-1, -1, region) #scan from bottom to top
    sides += scan_cols(min_c, max_c+1, 1, region) #scan from left to right
    sides += scan_cols(max_c, min_c-1, -1, region) #scan from  right to left
    return sides

#MAIN
with open("data/12f.txt") as file:
    lines = file.read().splitlines()

grid, max_r, max_c = create_grid(lines)

price_part1 = 0
price_part2 = 0
for region in grid.keys():
    while len(grid[region]) > 0:
        visited, perimeter = find_region_size_and_perimeter(grid[region])
        grid[region] = [item for item in grid[region] if item not in visited]
        price_part1 += len(visited) * perimeter
        price_part2 += count_sides(visited) * len(visited)
print("Part 1:", price_part1)
print("Part 2:", price_part2)
print("Total runtime:", datetime.now() - time_start)
