def inversions_div(A):
    if len(A) <= 1:
        return A, 0
    mid = len(A) // 2
    A_1, total1 = inversions_div(A[:mid])
    A_2, total2 = inversions_div(A[mid:])
    end_arr, tot = count(A_1, A_2)
    return end_arr, (tot+total1+total2)

def count(A_1, A_2):
    # A_1 is left, A_2 is right
    arr = []
    i, j = 0, 0
    total = 0
    inv_point = 0
    # print("A_1:",A_1,"A_2:",A_2)
    
    while i < len(A_1) and j < len(A_2):
        if A_1[i] > A_2[j]:
            inv_point += 1
            total += 1
            arr.append(A_2[j])
            j += 1
            # print("inversion at i={}, j={}".format(i, j))
        else:
            arr.append(A_1[i])
            i += 1
            if i < len(A_1): total += inv_point

    while i < len(A_1):
        arr.append(A_1[i])
        i += 1
        if i < len(A_1): total += inv_point
    while j < len(A_2):
        arr.append(A_2[j])
        j += 1
    
    # print("arr:",arr,"total:",total)
    return [arr, total]

arr = [1, 4, 5, 6, 7, 2, 8, 3]
new_arr, res = inversions_div(arr)
print(res)

print('starting')
arr = []
for i in range(1_000_000, 0, -1):
    arr.append(i)
new_arr, res = inversions_div(arr)
print(res)