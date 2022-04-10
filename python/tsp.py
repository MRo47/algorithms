from copy import deepcopy
import numpy as np

input_arr = ["FOOF", "OCOO", "OOOH", "FOOO"]

# convert input data into coordinates
def get_coords(arr: list):
    coords = {}
    print("Charlie: 1\nHome: 2")
    f_cnt = 3 #foods start from 3
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'F':
                coords[f_cnt] = [i, j]
                print("Food: ", f_cnt)
                f_cnt += 1
            elif arr[i][j] == 'C':
                coords[1] = [i, j] #charlie is 1
            elif arr[i][j] == 'H':
                coords[2] = [i, j] #home is 2 
    
    print("\nCoordinates: \n", coords)
    return coords

# cost between 2 nodes is manhattan distance
def cost_fn(coords_a, coords_b):
    return abs(coords_a[0] - coords_b[0]) + \
        abs(coords_a[1] - coords_b[1])

# computes cost between all nodes
def get_cost(coords: list, foods: list):
    cost = {}
    for i in foods:
        for j in foods:
            if i != j:
                if (j, i) in cost:
                    cost[i, j] = cost[j, i]
                else:
                    cost[i, j] = cost_fn(coords[i], coords[j])
        cost[1, i] = cost_fn(coords[1], coords[i])
        cost[i, 2] = cost_fn(coords[i], coords[2])

    print("\ncost fn")
    print(cost, "\n")
    return cost

# computes the minimum cost for sequence
def min_path_cost(start: str, coords: list, cost: dict, seen=[]):
    min_cost = np.inf
    seen.append(start)
    if len(seen) == len(coords)+1:
        return [start, 2], cost[seen[-1], 2]

    ret_seq = [start]

    for ci in coords:
        if ci not in seen:
            print("start: ", start, " end: ", ci)
            seq, cost_here = min_path_cost(ci, coords, cost, deepcopy(seen))
            cost_here += cost[start, ci]
            if cost_here < min_cost:
                min_cost = cost_here
                seq_at_min = seq

    print("min cost from: ", start, " is: ", min_cost, " seq: ", seq_at_min)
    ret_seq.extend(seq_at_min)
    
    return ret_seq, min_cost
        
# top level call
def solve(arr: list):
    coords = get_coords(arr)
    
    foods = sorted(coords)[2:]

    cost = get_cost(coords, foods)

    print("min: ", min_path_cost(1, foods, cost))

if __name__ == "__main__":
    solve(input_arr)
