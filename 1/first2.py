with open('input.txt') as f:
    content = f.readlines()
numbers = [int(x) for x in content]


def find_triplets(numbers, arr_size, sum): 
    for i in range(0, arr_size-2): 
        for j in range(i + 1, arr_size-1):  
            for k in range(j + 1, arr_size): 
                if numbers[i] + numbers[j] + numbers[k] == sum: 
                    print(numbers[i],numbers[j],numbers[k])
                    print(numbers[i]*numbers[j]*numbers[k])

sum = 2020
find_triplets(numbers, len(numbers), sum) 