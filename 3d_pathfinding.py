_='''
- imagine starting at the coordinate (n, a, b) in 3D space.
- (n, a, b) = ni + aj + bk
- each recursive step moves you 1 unit closer to 0 
- therefore, as you progress through the recursive steps, either n, a, or b is moved 1 unit closer to 0
- you reach (0, 0, 0) once n+a+b recursive steps have happened
- each recursive step writes 1 entry to memo
- therefore memory complexity = O(n + a + b)
- but a and b are each at most n -> O(n + n + n) -> O(3n) -> O(n)
'''

def memo_robot_paths(m, n): # runtime = O(mn), memory = O(mn)
    memo = {(0,1): 1, (1,1): 3}

    if (m,n) in memo: # calculations done
        return memo[(m,n)]
    elif (n,m) in memo: # calculations done
        return memo[(n,m)]
    
    elif m == 0 or n == 0: # on one of the walls
        return 1
    
    else: # we need to calculate
        # max recursions = O(m + n)
        p1 = memo_robot_paths(m-1, n)
        p2 = memo_robot_paths(m-1, n-1)
        p3 = memo_robot_paths(m, n-1)
        
        memo[(m,n)] = p1 + p2 + p3
        return (p1 + p2 + p3)

def robot_paths_3d(x, y, z):
    memo = {(1,0,0): 1, (0,1,0): 1, (0,0,1): 1}
    
    perms = [(x,y,z),(x,z,y),(y,x,z),(y,z,x),(z,x,y),(z,y,x)]
    intersect = set(memo.keys()) & set(perms)
    if intersect:
        return memo[intersect[0]]
    elif (x==0 and y==0) or (x==0 and z==0) or (y==0 and z==0):
        return 1
    elif x==0 or y==0 or z==0:
        s = []
        if x!=0:
            s.append(x)
        if y!=0:
            s.append(y)
        if z!=0:
            s.append(z)
        return memo_robot_paths(s[0], s[1])
    else:
        p1 = robot_paths_3d(x-1, y, z)
        p2 = robot_paths_3d(x, y-1, z)
        p3 = robot_paths_3d(x, y, z-1)
        memo[(x, y, z)] = p1+p2+p3
        return memo[(x,y,z)]

dave = robot_paths_3d(1, 1, 1)
print(dave)