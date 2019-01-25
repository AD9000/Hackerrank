'''
Author: Atharv Damle

# Question statement below from hackerrank (https://www.hackerrank.com/challenges/python-loops/problem)
Task 
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
'''

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        # (i ** 2) in python is the same as (i ^ 2) in maths.
        print(i**2)

