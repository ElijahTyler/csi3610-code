# lambda defines an anonymous function
# ex. ratio = lambda t: t[0]/t[1]
# ratio((5, 2)) -> returns 2.5

def fractional_knapsack(items, W):
    items.sort(key = lambda t: -t[0]/t[1])
    print(items)
    max_value = 0

    for value, weight in items: # enter up to n times -> O(n)
        if weight <= W:
            max_value += value
            W -= weight
        else:
            fraction = W / weight
            max_value += value*fraction
            return max_value
    
    return max_value

paul = fractional_knapsack([(3,3),(4,6),(7,10)], 10)
print(paul)

# memory complexity: O(1)