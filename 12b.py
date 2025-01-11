# Function to calculate the sides and area for each individual region
def calculate_individual_region_results(grid, target_letter):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    regions_results = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_within_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # DFS to explore a region and calculate its sides and area
    def dfs(x, y):
        stack = [(x, y)]
        area = 0  # Number of cells with the target_letter
        sides = 0  # Perimeter of the current region
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            area += 1

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if not is_within_bounds(nx, ny) or grid[nx][ny] != target_letter:
                    sides += 1  # Boundary detected
                elif (nx, ny) not in visited:
                    stack.append((nx, ny))

        return area, sides

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == target_letter and (i, j) not in visited:
                area, sides = dfs(i, j)
                regions_results.append(area * sides)

    return regions_results


# Input map data
map_data = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

grid = [list(row) for row in map_data]

# List of region letters to analyze
regions = ["R", "C", "I", "F", "V", "J", "E", "M", "S"]

# Calculate results for each letter
detailed_results = {}
for region in regions:
    detailed_results[region] = calculate_individual_region_results(grid, region)

# Print results
total = 0
for region, results in detailed_results.items():
    for result in results:
        total += result
    print(f"Region '{region}': {results}")

print(total)