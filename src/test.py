from resources import Train, create_line, create_train, get_lines, get_trains
from math import sqrt

print("-----[THE LINES]-----")
get_lines()
print()
print("-----[THE TRAINS]-----")
get_trains()

# Comparing ONE train across MULTIPLE lines
list_total = []
names = []
# Choosing the train
choice_train = int(input("Pick your train: ")) - 1
with open("trains.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i == choice_train:
            attr = line.split("/")
            train = Train(attr[0], attr[1], attr[2], attr[3])
# Assigning values to the different units
a = float(train.get_acceleration())
v = float(train.get_speed())
r = float(train.get_retardation())
s0 = int((v**2)/(2*a))
s1 = int((v**2)/(2*r))
# Choosing the different lines
amount = int(input("How many lines do you want to compare (1 if you just want to calculate for a single line)? "))
z = 0
y = 0
lines = [[] for i in range(amount)]
for y in range(amount):
    line_number = 1
    choice_line = int(input(f"Line nr{line_number}: ")) - 1
    line_number += 1
    with open("lines.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == choice_line:
                stats = line.split(",")
                names.append(stats[0][1:])
                x = 1
                for i in range(int(len(stats)-2)):
                    lines[z].append(eval(stats[x]))
                    x += 1
                if amount - y != 1:
                    lines[z].append(eval(stats[x][:-2]))
                else:
                    lines[z].append(eval(stats[x][:-1]))
        
        # Calculating the time it takes and printing it out.
        print(lines[z])
        z += 1
