#!/bin/python3
'''
This question is the User-Friendly Password System problem
as part of a mock practice for TikTok OA on HackerRank'''

import os

def pwd_hash(s):
    n = len(s)
    M = 10 ** 9 + 7
    p = 131
    h = 0
    power = 1
    for i in range(n - 1, -1, -1): # iterate from the last character
        h = (h + ord(s[i]) * power) % M # modulo at every addition to prevent overflow
        # reduce the size of intermediate values
        power = (power * p) % M
        # exponentiation by iteration
    return h

def authEvents(events):
    P = 131
    M = 10 ** 9 + 7
    password_hash = None 
    results = []

    for event_type, event_param in events:
        if event_type == "setPassword":
            password_hash = pwd_hash(event_param)

        elif event_type == "authorize":
            if password_hash is None:
                results.append(0)
                continue

            attempted_hash = int(event_param)
            # Exact match check
            if attempted_hash == password_hash:
                results.append(1)
                continue

            # Single character appended hash check
            found = False
            # use for loop instead of subtracting appended hash from password hash
            # to avoid modulo wrap-around and hash collisions
            # hash collisions: 2 different values with the same hash
            for c in range(32, 128):  # ASCII range for valid characters
                appended_hash = (password_hash * P + c) % M
                if appended_hash == attempted_hash:
                    found = True
                    break
            results.append(1 if found else 0)

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())
    print(events)

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

'''
Test case 1:
Input:
4
2
setPassword 000A
authorize 108738450
authorize 108738449
authorize 244736787
-------------------
Expected Output
0
1
1
'''

'''
Test case 2
8
2
setPassword a
authorize 97
authorize 12756
authorize 12804
authorize 12829
authorize 12772
authorize 12797
authorize 98
-------------------
Expected Output
1
1
1
1
1
1
0
'''