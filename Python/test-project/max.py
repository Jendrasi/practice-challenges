numbers = [210, 4, 7, 53, 15, 95, 209]
max = numbers[0]
for num in numbers[1:]:
    if num > max:
        max = num
print("Max is", max)