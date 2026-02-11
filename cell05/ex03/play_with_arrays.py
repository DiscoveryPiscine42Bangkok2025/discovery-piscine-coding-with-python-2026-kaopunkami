#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]

result = set()
for x in arr:
    if x > 5:
        result.add(x + 2)

print(arr)
print(result)