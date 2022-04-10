from copy import deepcopy
import numpy as np

input_arr = ["FOOF", "OCOO", "OOOH", "FOOO"]

def get_coords(arr: list):
    coords = {}
    foods = []
    print("Charlie: 1\nHome: 2")
    cnt = 3 #foods start from 3
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 'F':
                foods.append(cnt)
                coords[foods[-1]] = [i, j]
                print("Food: ", cnt)
                cnt += 1
            elif arr[i][j] == 'C':
                coords[1] = [i, j] #charlie is 1
            elif arr[i][j] == 'H':
                coords[2] = [i, j] #home is 2 
    
    print("\nCoordinates: \n", coords)
    return coords, foods

def cost_fn(coords_a, coords_b):
    return abs(coords_a[0] - coords_b[0]) + \
        abs(coords_a[1] - coords_b[1])

def get_cost(coords: list, foods: list):
    print("\ncost fn")
    cost = {}
    for i in foods:
        for j in foods:
            if i != j:
                if (j, i) in cost:
                    cost[(i, j)] = cost[j, i]
                else:
                    cost[(i, j)] = cost_fn(coords[i], coords[j])

    for i in foods:
        cost[(1, i)] = cost_fn(coords[1], coords[i])
        cost[(i, 2)] = cost_fn(coords[i], coords[2])

    print(cost)
    return cost


def min_path_cost(start: str, coords: list, cost: dict, seen=[]):
    min_cost = np.inf
    seen.append(start)
    print("\nseen: ", seen)
    if len(seen) == 4:
        print("end")
        return cost[(seen[-1], 2)]

    for ci in coords:
        if ci not in seen:
            print("start: ", start, " end: ", ci)
            min_cost = min(
                min_cost,
                cost[(start, ci)] +
                min_path_cost(ci, coords, cost, deepcopy(seen))
            )
    
    return min_cost
        

def solve(arr: list):
    coords, foods = get_coords(arr)
    
    cost = get_cost(coords, foods)

    print("min: ", min_path_cost(1, sorted(coords)[2:], cost))


solve(input_arr)
