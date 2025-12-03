arr = [2, 5, 7,11, 31,10]
target = 10

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("Linear Search: Found at index", i)
        found = True
        break

if not found:
    print("Linear Search: Not Found")
