Liste = [1, 2, 3, 4, 5]
temp = Liste[0]
Liste[0] = Liste[-1]
Liste[-1]= temp
print(Liste)