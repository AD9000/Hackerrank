import re

s = input()
k = input()

# Create regex pattern (here, the string k)
p = re.compile(k)

# Search for pattern in 's'
m = p.search(s)

# If m is null,
if not m:
    print ((-1, -1))
    
else:

    # While m exists,
    while m:
        print((m.start(), m.end() - 1))
        
        # Search again, skipping the first character of the last search
        m = p.search(s, m.start() + 1)

