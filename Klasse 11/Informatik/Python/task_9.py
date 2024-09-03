import io

array = []
with io.open("source.txt") as file:
    for line in file.readlines():
        array.append([float(num) for num in line.split(',')])
    file.close()
print(array)