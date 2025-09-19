a = [12,13,18,15,16]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")