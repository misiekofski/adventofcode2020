with open('input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

def count_letters(password):
    letter_occurences = {}
    for letter in password:
        letter_occurences[letter] = password.count(letter)
    return letter_occurences

def get_policy(policy):
    policy = password[0].split(" ")
    letter = policy[1]
    minmax = policy[0].split("-")
    min = minmax[0]
    max = minmax[1]
    return { letter : (min, max)}

valid_passwords = 0

for line in lines:
    password = line.split(": ")
    letters = count_letters(password[1])
    # print(letters)
    policy = get_policy(password[0])
    # print(policy)
    
    for key,value in policy.items():
        min = int(value[0])
        max = int(value[1])
        letter = key
        try:
            if letters[key] >= min and letters[key] <=max:
                valid_passwords += 1
        except:
            pass

print(valid_passwords)