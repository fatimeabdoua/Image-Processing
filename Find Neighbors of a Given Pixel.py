#Find 4-neighbors
from functools import update_wrapper

def find_4_neighbors(x, y, width, height):
    neighbors = []
    if x > 0: #left
        neighbors.append((x-1, y))
    if x < width - 1: #right
        neighbors.append((x+1, y))
    if y > 0: #up
        neighbors.append((x, y-1))
    if y < height - 1: #down
        neighbors.append((x, y+1))
        return neighbors

#Find 4 diagonal neighbors

def find_4_diagonal_neighbors(x, y, width, height):
    neighbors = []
    if x > 0 and y > 0: # top-left
        neighbors.append((x-1, y-1))
    if x > 0 and height < - 1: #Bottom-left
        neighbors.append((x-1, y+1))
    if x < width - 1 and y > 0: # top-right
        neighbors.append((x+1, y-1))
    if x < width - 1 and y < height - 1: #bottom-right
        neighbors.append((x+1, y+1))
        return neighbors

#Find 8 neighbors
def find_8_neighbors(x, y, width, height):
    neighbors = find_4_neighbors(x, y, width, height) + find_4_diagonal_neighbors(x, y, width, height)
    return neighbors

# example

width = 7
height = 7

x, y = 3,3 # pixel at (3,3)

print("4-Neighbors:", find_4_neighbors(x, y, width, height))
print("4-Diagonal Neighbors:", find_4_diagonal_neighbors(x, y, width, height))
print("8-Neighbors:", find_8_neighbors(x, y, width, height))
