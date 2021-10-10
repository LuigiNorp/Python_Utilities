l1 = [10, 20, 30, 40, 50]
l3 = [50, 75, 30, 20, 40, 69]

res = [x for x in l1 + l3 if x not in l1 or x not in l3]

print(res)
if not res:
    print("Lists l1 and l3 are equal")
else:
    print("Lists l1 and l3 are not equal")