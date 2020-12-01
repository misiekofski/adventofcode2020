with open('input.txt') as f:
    content = f.readlines()
numbers = [int(x) for x in content]

for i, number in enumerate(numbers[:-1]):
    complementary = 2020 - number
    if complementary in numbers[i+1:]:
        print(f"Solution Found: {number} and {complementary}")
        print(number*complementary)
        break