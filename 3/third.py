with open('input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
multipled_lines = []

x_slope = 1
y_slope = 2
trees = 0
x = 0

for i in range(len(lines)):
    multipled_lines.append(lines[i] * x_slope * 11)

for i in range(0, len(multipled_lines), y_slope):
    if multipled_lines[i][x] == "#":
        trees +=1
    x += x_slope

print(trees)