def solution(x, a):

    num_of_x = 0
    for i, elem in enumerate(a):
        if elem == x:
            num_of_x += 1
        a[i] = num_of_x

    num_of_non_x = 0
    if a[-1] == 0:
        return len(a)
    if a[-1] == len(a):
        return 0
    for i in range(len(a) - 1, 0, -1):
        if a[i] == a[i - 1]:
            num_of_non_x += 1
        if num_of_non_x == a[i]:
            return i
    return len(a) - num_of_non_x

if __name__ == "__main__":
    x = 5
    a = [2,2,3,4,4,5,4,5,5,5,5]
print(solution(x, a))