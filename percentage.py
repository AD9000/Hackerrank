if __name__ == '__main__':
    # Accept input (As a dictionary)
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    # Accept name of student to be found
    query_name = input()
    
    # Average students marks and print it. Formatting it to 2 decimal plaves. 
    print("%0.2f"%(sum(student_marks.get(query_name, None))/len(student_marks.get(query_name, None))))
