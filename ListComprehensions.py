if __name__ == '__main__':
    # Accept 4 numbers.
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    
    # Print [a, b, c] for each possible combination of a, b and c if (a + b + c) is not equal to n. 
    # This is actually accomplished as a O(n^3) complexity nested loop.
    print ([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])

