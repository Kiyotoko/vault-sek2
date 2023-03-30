sqares = { 

}

for i in range(1, 10):
    sqares[i] = i**2

print(str(sqares).replace('{', '{\n\t').replace(', ', ',\n\t').replace('}', '\n}'))