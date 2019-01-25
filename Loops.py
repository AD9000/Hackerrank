'''
Author: Atharv Damle

# For complete Question statement go to hackerrank (https://www.hackerrank.com/challenges/python-loops/problem)
# Copyright issues don't allow me to display it here...

# tldr; Print square of numbers from 1 to n. (Use exponential operator)
'''

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        # (i ** 2) in python is the same as (i ^ 2) in maths.
        print(i**2)

