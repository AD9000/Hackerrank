if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m = [-101, -101]

    for i in arr:
        if (i > m[0]):
            m[1] = m[0]
            m[0] = i
        elif (i > m[1] and m[0] != i):
            m[1] = i
    
    print(m[1])

