
elements = [1, 2, [3 , 4, 5, 6], 7, 8]

counter = 2
for e in elements[2]:
    elements.insert(counter, e)
    counter += 1
    print(elements)