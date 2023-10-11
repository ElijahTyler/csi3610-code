# random points
def number_generator():
    a = 290797
    while True:
        yield a
        a = a * a % 50515093

def random_points():
    points = []
    gen = number_generator()
    for i in range(2_000_000):
        points.append((next(gen), next(gen)))
    return points

# merge sort
def merge(a_1, a_2, axis):
    result = []
    i, j = 0, 0
    while i < len(a_1) and j < len(a_2):
        if a_1[i][axis] <= a_2[j][axis]:
            result.append(a_1[i])
            i += 1
        else:
            result.append(a_2[j])
            j += 1
    while i < len(a_1):
        result.append(a_1[i])
        i += 1
    while j < len(a_2):
        result.append(a_2[j])
        j += 1
    return result

def merge_sort(a, index):
    if len(a) == 1:
        return a
    midpt = len(a) // 2
    a_1 = merge_sort(a[:midpt], index)
    a_2 = merge_sort(a[midpt:], index)
    return merge(a_1, a_2, index)



# minimum distance
def euclid(a, b):
    e_a = (b[0]-a[0])**2
    e_b = (b[1]-a[1])**2
    return (e_a + e_b)**0.5

def minimum_distance(P, X, Y):
    #base case
    if len(P) <= 1:
        return (0,0), (0,0), float('inf')
    elif len(P) in [2, 3]:
        dist1 = euclid(P[0], P[1])
        if len(P) == 2:
            return P[0], P[1], dist1
        else:
            dist2 = euclid(P[0], P[2])
            dist3 = euclid(P[1], P[2])
            if dist2 < dist1:
                if dist3 < dist2:
                    return P[1], P[2], dist3
                return P[0], P[2], dist2
            return P[0], P[1], dist1
    else:
        # recursive case
        mid_index = (len(X)) // 2
        mid_line = X[mid_index][0]
    
        # divide
        PL, PR = [], []
        for p in range(len(P)):
            if P[p][0] <= mid_line:
                PL.append(P[p])
            else:
                PR.append(P[p])
    
        XL, XR = [], []
        for p in range(len(X)):
            if X[p][0] <= mid_line:
                XL.append(X[p])
            else:
                XR.append(X[p])
    
        YL, YR = [], []
        for p in range(len(Y)):
            if Y[p][0] <= mid_line:
                YL.append(Y[p])
            else:
                YR.append(Y[p])

        # conquer
        Lpt_a, Lpt_b, deltaL = minimum_distance(PL, XL, YL)
        Rpt_a, Rpt_b, deltaR = minimum_distance(PR, XR, YR)
        if deltaL < deltaR:
            pt_a = Lpt_a
            pt_b = Lpt_b
            delta = deltaL
        else:
            pt_a = Rpt_a
            pt_b = Rpt_b
            delta = deltaR
    
        # combine
        Y_prime = []
        for p in range(len(Y)):
            if (mid_line - delta) <= Y[p][0] and Y[p][0] <= (mid_line + delta):
                Y_prime.append(Y[p])
    
        for p in range(len(Y_prime)):
            j = 1
            while (not (p+j) == len(Y_prime)) and j <= 7:
                delta_temp = euclid(Y_prime[p], Y_prime[p + j])
                if delta_temp < delta:
                    pt_a = Y_prime[p]
                    pt_b = Y_prime[p + j]
                    delta = delta_temp
                j += 1
    
        return pt_a, pt_b, delta
    


# test case
pts = random_points()

X = merge_sort(pts, 0)
print("merge sorted X")

Y = merge_sort(pts, 1)
print("merge sorted Y")

pt_a, pt_b, res = minimum_distance(pts, X, Y)
print("best points:", pt_a, pt_b)
print("min distance:", res)