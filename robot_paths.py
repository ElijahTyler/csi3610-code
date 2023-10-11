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

res = memo_robot_paths(4, 5)
print(res)



def array_robot_paths(m='width', n='height'): # runtime = THETA(mn), memory = THETA(mn)
    paths = [[0]*(m+1) for _ in range(n+1)]
    for i in range(m+1):
        paths[0][i] = 1
    for i in range(n+1):
        paths[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            paths[i][j] = paths[i-1][j] + paths[i][j-1] + paths[i-1][j-1] # key formula
    return paths[n][m]

paul = array_robot_paths(4, 5)
print(paul)