def select_max(A, left, right):
    max_pos = left

    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i
        i = i + 1

    return max_pos

def select_sort(A):
    for i in range(len(A) - 1, 0, -1):
        index = select_max(A, 0, i)
        if index != i:
            tmp = A[index]
            A[index] = A[i]
            A[i] = tmp

def invert_vector(A):
    i = 0
    j = len(A) - 1
    while i <= (len(A) - 1)/2:
        h = j - i
        A[i], A[h] = A[h], A[i]

        i = i + 1
    return A



if __name__ == "__main__":
    numbers = [12, 2, 4, 18, 6, 5]
    # n = select_max(numbers, 0, len(numbers) - 1)
    # print(n)
    # select_sort(numbers)
    # print(numbers) 

    print(invert_vector(numbers))
    #swp
    # a = 10
    # b = 27
    # print(a, b)
    # a,b = b, a
    # print(a, b)
