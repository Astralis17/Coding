

numbers = [0,1]
for i in range(10000):
        numbers.append(sum(numbers[-2:]))
print(numbers[-1])

