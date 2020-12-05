import re 

with open('input.txt') as f:
    lines = f.readlines()

i = 0
passports = {}
expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

linijka = ""
for line in lines:
    x = []
    if line=="\n" or line=="":
        i+=1
        linijka = ""
        continue
    else:
        linijka = linijka + " " + line.strip()
    passports[i] = re.findall(r'(\w+) *:(?: *([\w.-]+))?', linijka)

def get_tuple_names(l):
    result = []
    for t in l:
        result.append(t[0])
    return result

def check_passport_keys():
    number_of_valid_passwords = 0
    for v in passports.values():
        actual = get_tuple_names(v)
        if set(expected).issubset(actual):
            number_of_valid_passwords += 1
    return number_of_valid_passwords

print(check_passport_keys())