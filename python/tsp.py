from copy import deepcopy
import numpy as np

input_arr = ["COOC", "OSOO", "OOOH", "COOO"]

# convert input data into coordinates
def get_coords(arr: list):
    coords = {}
    key = {
        1: 'S', #salesman is 1
        2: 'H' #home is 2
    }

    f_cnt = 3 #foods start from 3
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'C':
                coords[f_cnt] = [i, j]
                key[f_cnt] = "C{},{}".format(i, j)
                f_cnt += 1
            elif arr[i][j] == 'S':
                coords[1] = [i, j]
            elif arr[i][j] == 'H':
                coords[2] = [i, j]
    
    print("\nCoordinates: \n", coords)
    print("\nkey: ", key)
    return coords, key

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
    coords, key = get_coords(arr)
    
    foods = sorted(coords)[2:]

    cost = get_cost(coords, foods)

    min_path, min_cost = min_path_cost(1, foods, cost)

    print("\nResult:")
    print("min path: ")
    for node in min_path:
        print(key[node])
    
    print("cost for min path: ", min_cost)


if __name__ == "__main__":
    solve(input_arr)
