'''
Author: Atharv Damle

#Question Statement on hackerrank (https://www.hackerrank.com/challenges/python-print/problem)

# tl:dr; print numbers from 1 to n without spaces
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print((i+1), end="")

    # The print statement below just moves the control to the next line
    print()
