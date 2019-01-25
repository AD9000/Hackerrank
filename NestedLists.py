if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        data.append([input(), float(input())])
    
    scores = sorted({i[1] for i in data})
    res = sorted([i[0] for i in data if i[1] == scores[1]])
    for i in res:
        print(i)
