if __name__ == '__main__':
    data = []
    # Accept input in an empty list
    for _ in range(int(input())):
        data.append([input(), float(input())])
    
    # Sort the first elements of each sublist and store in a set.
    scores = sorted({i[1] for i in data})
    
    # solution is a sorted list of names of people with the second highest score (ie scores[1]. scores[0] is highest)
    res = sorted([i[0] for i in data if i[1] == scores[1]])
    for i in res:
        print(i)
