with open('input.txt') as f:
    lines = f.readlines()

max_column = 7
max_row = 127

for line in lines:
    seat_directions = [c for c in line.strip("\n")]