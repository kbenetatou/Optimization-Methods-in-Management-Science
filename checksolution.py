from solution import result,demand,each_cost, euclidean_distances, calculate_cost,rr
best_solution = None
best_cost = float('inf')
better_result = []
better_cost = []

for i, current_solution in enumerate(result):
    current_cost = each_cost[i]
    
    for j in range(1, len(current_solution) - 1):
        new_solution = current_solution.copy()
        new_solution[j], new_solution[j + 1] = new_solution[j + 1], new_solution[j]
        new_cost = calculate_cost(new_solution, demand, euclidean_distances,rr[i])

 
        if new_cost < current_cost:
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
    if best_solution != None:
        better_result.append(best_solution)
        better_cost.append(best_cost)
    else:
        better_result.append(current_solution)
        better_cost.append(current_cost)

    best_solution = None
    best_cost = float('inf')
   
number_of_lists = len(better_result)
better_cost_sum = sum(better_cost)

print(f"The first solution has a cost of z: {sum(each_cost)}")
print(f"The optimized solution has a cost of z: {better_cost_sum}")

def save_solution(better_result, q, better_cost_sum, file_name='final_solution_better.txt'):
    with open(file_name, 'w') as file:
        file.write('Cost:\n')
        file.write(str(better_cost_sum) + '\n')
        file.write('Routes:\n')
        file.write(str(q) + '\n')
        for route in better_result:
            file.write(','.join(map(str, route)) + '\n')
 
save_solution(better_result,number_of_lists, better_cost_sum)