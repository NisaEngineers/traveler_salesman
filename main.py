import itertools  # Used to generate all possible city visit permutations

# 🗺️ Distance matrix: symmetric 2D list where distances[i][j] is the distance from city i to city j
# Example: 4 cities with manually defined distances
distances = [
    [0, 10, 15, 20],  # Distances from city 0 to others
    [10, 0, 35, 25],  # Distances from city 1 to others
    [15, 35, 0, 30],  # Distances from city 2 to others
    [20, 25, 30, 0]   # Distances from city 3 to others
]

# 🧮 Function to calculate total distance of a given route
def calculate_total_distance(route, distance_matrix):
    total = 0
    # Sum distances between consecutive cities in the route
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    # Add distance to return to the starting city (complete the cycle)
    total += distance_matrix[route[-1]][route[0]]
    return total

# 🚀 Brute-force TSP solver: tries all possible routes starting from city 0
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)           # Number of cities
    cities = list(range(n))            # City indices: [0, 1, 2, ..., n-1]
    min_distance = float('inf')        # Initialize with infinity
    best_route = None                  # To store the best route found

    # Generate all permutations of cities excluding the starting city (city 0)
    for perm in itertools.permutations(cities[1:]):
        route = [0] + list(perm)       # Fix city 0 as the starting point
        dist = calculate_total_distance(route, distance_matrix)
        # Update best route if a shorter one is found
        if dist < min_distance:
            min_distance = dist
            best_route = route

    return best_route, min_distance

# 🧪 Run the TSP solver
route, distance = tsp_brute_force(distances)

# 📢 Output the result
print("Best route:", route)           # Example: [0, 1, 3, 2]
print("Minimum distance:", distance)  # Example: 80
