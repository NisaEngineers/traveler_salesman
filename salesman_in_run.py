import itertools

# 🏙️ City names for reference
cities = ["New York", "Los Angeles", "Chicago", "Houston"]

# 📏 Distance matrix (in kilometers)
distances = [
    [0, 3935, 1145, 2282],     # New York
    [3935, 0, 2805, 2450],     # Los Angeles
    [1145, 2805, 0, 1515],     # Chicago
    [2282, 2450, 1515, 0]      # Houston
]

# 🧮 Calculate total distance for a route
def calculate_total_distance(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    total += distance_matrix[route[-1]][route[0]]  # return to start
    return total

# 🚀 Brute-force TSP solver
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    city_indices = list(range(n))
    min_distance = float('inf')
    best_route = None

    for perm in itertools.permutations(city_indices[1:]):
        route = [0] + list(perm)
        dist = calculate_total_distance(route, distance_matrix)
        if dist < min_distance:
            min_distance = dist
            best_route = route

    return best_route, min_distance

# 🧪 Run the solver
best_route_indices, min_distance = tsp_brute_force(distances)
best_route_names = [cities[i] for i in best_route_indices]

# 📢 Output
print("Best route:", " → ".join(best_route_names))
print("Minimum distance:", min_distance, "km")
