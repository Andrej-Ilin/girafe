def maximum_cost_of_sand(N, W, bunches):
    # Calculate cost to weight ratio and store it with its cost and weight
    bunches_with_ratios = []
    free_money = 0  # To accumulate free money from zero weight bunches
    
    for cost, weight in bunches:
        if weight == 0 and cost > 0:
            # Free money case
            free_money += cost
        elif weight > 0:  # Avoid division by zero
            ratio = cost / weight
            bunches_with_ratios.append((ratio, cost, weight))
    
    # Sort bunches based on cost to weight ratio in descending order
    bunches_with_ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_cost = free_money  # Start with the free money
    remaining_weight = W
    
    for ratio, cost, weight in bunches_with_ratios:
        if remaining_weight <= 0:
            break
        
        if weight <= remaining_weight:
            # Take the whole bunch
            total_cost += cost
            remaining_weight -= weight
        else:
            # Take the fraction of the bunch that fits
            total_cost += (cost * remaining_weight // weight)
            remaining_weight = 0  # Now the bag is full
    
    return total_cost

# Input reading
N, W = map(int, input().split())
bunches = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the maximum cost
result = maximum_cost_of_sand(N, W, bunches)
print(result)