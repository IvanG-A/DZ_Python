def square(side):
    area = side * side
    if area != int(area):
        return int(area) + 1
    return int(area)

print(square(6))
print(square(21))