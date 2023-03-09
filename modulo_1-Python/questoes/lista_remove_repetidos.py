a = [1,2,4,9,3,5]
b = [7,2,9,10,-1,3]
c = []

for element in a+b:
    if not element in a or not element in b:
        c.append(element)

print(c)
