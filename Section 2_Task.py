"""
***input***
5
7
compass 0.5 6
hatchet 1.5 5
matches 0.4 4
tarpaulin 1 4
telescope 1.1 3
cylinder 1.6 4
Rilakkuma 0.8 1
"""

limit = int(input("Write the limit: "))
t = int(input("Enter Number of Items: "))
print("Write item name - item weight - item value")

ratios = []

def Solver(ratios, limit):
    ratios = sorted(ratios, key=lambda x: x[1],reverse=True)

    for j in ratios:
        if limit >= float(j[2]) and limit != 0:
            limit -= float(j[2])
            print(f"YOU CAN TAKE: {j[0]}")
        else:
            break

for i in range(t):
    item, weight, value = input().split()
    ratio = float(value) / float(weight)
    ratios.append([item,ratio,weight])

# call function
Solver(ratios,limit)
