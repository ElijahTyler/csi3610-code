'''
(2, 1): 1, (1, 2): 1, (-1, 2): 1, (-2, 1): 1, (-2, -1): 1, (-1, -2): 1, (1, -2): 1, (2, -1): 1



Knight Moves
Precondition: An ordered pair of integers are passed into the function.
Postcondition: The function returns the number of knight moves to the square.

idea:

how many moves can a knight make on an infinite chessboard? always 8
therefore, make 8 recursive calls on each level until the square is hit
T(n) = 8T(n/?) + f(n)

optimization:
- let V be a vector from the initial square to the goal square
- let K1...K8 be the 8 vectors of possible knight moves
- out of K1...K8, discard the vectors that make more than a 90 degree angle with V


'''
from math import acos, pi

# a dot b = a[0]b[0] + a[1]b[1] = magnitude(a) * magnitude(b) * cos(theta)
def angle(a=(0,0), b=(0,0)):
    va = magnitude(a[0], a[1])
    vb = magnitude(b[0], b[1])
    theta = acos( (a[0]*b[0] + a[1]*b[1]) / (va * vb) ) * (180/pi)
    return theta

def magnitude(x, y): # O(1)
    return (x**2 + y**2)**0.5

def knight_moves(x=0, y=0, memo={}, visited=list(), move_count=0, last_dx=0, last_dy=0):
    visited.append((x, y))
    # base cases
    if (abs(x) == 1 and abs(y) == 2) or (abs(x) == 2 and abs(y) == 1):
        return move_count + 1
    elif abs(x) == 1 and abs(y) == 1:
        return move_count + 2
    elif (abs(x) == 1 and abs(y) == 0) or (abs(x) == 0 and abs(y) == 1):
        return move_count + 3
    # memo case
    elif (x,y) in memo:
        return move_count + memo[(x,y)]
    elif (y,x) in memo:
        return move_count + memo[(y,x)]
    
    # recursive case
    best = float('inf')
    for dx, dy in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
        if angle((dx, dy), (x,y)) < 90 and (dx, dy) != (last_dx, last_dy) and (x-dx, y-dy) not in visited:
            k = knight_moves(x-dx, y-dy, memo, visited, move_count+1, dx, dy) # +1 indicates 1 move made
            if k < best:
                best = k

    memo[(x,y)] = best
    return memo[(x,y)]



paul = knight_moves(100,100)
print(paul)