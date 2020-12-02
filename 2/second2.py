with open('input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

def get_policy(policy):
    policy = password[0].split(" ")
    letter = policy[1]
    postitions = policy[0].split("-")
    return (letter, int(postitions[0]), int(postitions[1]))

valid_passwords = 0

for line in lines:
    password = line.split(": ")
    policy = get_policy(password[0])
    is_password_valid = False
    if password[1][policy[1]-1]==policy[0] or password[1][policy[2]-1]==policy[0]:
        is_password_valid = True
    if password[1][policy[1]-1]==policy[0] and password[1][policy[2]-1]==policy[0]:
        is_password_valid = False
    if (is_password_valid):
        valid_passwords += 1

print(valid_passwords)