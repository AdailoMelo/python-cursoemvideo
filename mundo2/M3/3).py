cont = 0
for i in range(1, 500, 2):
    if i % 2 != 0:
        if i % 3 == 0:
            cont += i
print(cont)
