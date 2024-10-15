import csv
import copy
import random
import numpy as np
file_path = 'Instance.txt'
customers = 250
capacity = 8
with open(file_path, 'r') as file:
    file_content = file.read()
lines = file_content.splitlines()
# Skip header lines
header_lines = 5  # Assuming there are 5 header lines
data_lines = lines[header_lines:]
# Creating a CSV reader
csv_reader = csv.reader(data_lines)
# Converting the CSV data into a 2D NumPy array
data_array = np.array(list(csv_reader), dtype=float)
# Extracting the x and y coordinates
coordinates = data_array[:, 1:3]
# Calculating the Euclidean distances for all nodes and appending them into a matrix
euclidean_distances = np.linalg.norm(coordinates - coordinates[:, np.newaxis], axis=2)
# c being the cost
c = euclidean_distances.copy()
# calculating s -> pairs of i,j
s = c[:, 0][:, np.newaxis] + c[0, :] - c
np.fill_diagonal(s, 0)
# Find the indices of non-zero elements
non_zero_indices = np.nonzero(s)
# Create a list containing the non-zero values and their corresponding indices
non_zero_values_indices = list(zip(s[non_zero_indices], zip(*non_zero_indices)))
# Sorting the list in descending order without the 0
sorted_non_zero_values_indices = sorted(non_zero_values_indices, key=lambda x: x[0], reverse=True)
# Extract the sorted non-zero values and their corresponding indices
sorted_non_zero_values = [value for value, indices in sorted_non_zero_values_indices]
sorted_non_zero_indices = [indices for value, indices in sorted_non_zero_values_indices]
printed_indices = set()
positions = [] #getting the final positions of pairs(i,j) that are sorted in decending order
for value, (i, j) in zip(sorted_non_zero_values, sorted_non_zero_indices):
    if (j, i) not in printed_indices:
        printed_indices.add((i, j))
        positions.append((i, j))
 
def clarke_wright_heuristic(positions, capacity_limit, capacity_matrix, customers):
    # creating the {0,1}, ... , {0,250}
    routes = [[0, i] for i in range(1,customers+1)]
    final_capacity = []
 
    # getting the last column of data_array as the "capacity"
    capacities = capacity_matrix[:, -1]
    for i in range(len(positions)):
            connection = [positions[i][0], positions[i][1]]
            
            route_i, route_j = None, None
            route_i_candidates = [route for route in routes if connection[0] in route]
            route_j_candidates = [route for route in routes if connection[1] in route]
            route_i = route_i_candidates[0] if route_i_candidates else None
            route_j = route_j_candidates[0] if route_j_candidates else None
           
            # checks if clients i, j are first or last.
            if route_i is not None and route_j is not None and route_i != route_j:
                if route_i[0] == connection[0] or route_i[-1] == connection[0]:
                    if route_j[0] == connection[1] or route_j[-1] == connection[1]:
                        new_route = route_i + [element for element in route_j if element not in route_i]
            
                        # checking the capacity (demand) of each customer
                        total_capacity = 0
                        
                        for index in new_route:
 
                            if index!=0:
                                total_capacity += capacities[index]
                                    
                        if total_capacity < 8:
                            route_i_index = next((index for index, route in enumerate(routes) if route == route_i), None)
                            routes.pop(route_i_index)
                            route_j_index = next((index for index, route in enumerate(routes) if route == route_j), None)
                            routes.pop(route_j_index)
                            routes.append(new_route)
                        else:
                            total_capacity = 0

    for i in range(len(routes)) :
        tc = 0
        for j in routes[i] :
            if j!=0:
                tc += capacities[j]
        final_capacity.append(tc)
            
    return routes, final_capacity
result, rr = clarke_wright_heuristic(positions, capacity, data_array, customers)

number_of_lists = len(result)
demand = data_array[:, -1]
cost = []
def calculate_cost(result, demand, distance_matrix,final_capacity):
        total_cost = 0
        total_demand = final_capacity + 6

        for i in range(len(result) - 1):
            current_element = result[i]
            next_element = result[i + 1]
            total_distance = distance_matrix[current_element][next_element]
            total_cost += (total_demand) * total_distance
            total_demand -= demand[next_element]

        return total_cost
z = 0
each_cost= []
for i in range(len(result)) :
    each_cost.append(calculate_cost(result[i],demand,euclidean_distances,rr[i]))
    z += calculate_cost(result[i],demand,euclidean_distances,rr[i])
def save_solution(routes, q, z, file_name='final_solution.txt'):
    with open(file_name, 'w') as file:
        file.write('Cost:\n')
        file.write(str(z) + '\n')
        file.write('Routes:\n')
        file.write(str(q) + '\n')
        for route in routes:
            file.write(','.join(map(str, route)) + '\n')
 
save_solution(result,number_of_lists, z)