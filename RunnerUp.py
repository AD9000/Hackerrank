if __name__ == '__main__':
    
    # Accept input
    n = int(input())
    arr = map(int, input().split())
    
    # Make a list to store two numbers: the largest and the second largest
    m = [-101, -101]

    # for each element in input. (Which is the scores list)
    for i in arr:
        # if element is greater than the largest element in m
        if (i > m[0]):
            # largest is now second largest.
            m[1] = m[0]
            m[0] = i
            
        # if the element is greater than the second largest but not the largest.
        elif (i > m[1] and m[0] != i):
            m[1] = i
    
    # Print solution: Second largest element in m
    print(m[1])

