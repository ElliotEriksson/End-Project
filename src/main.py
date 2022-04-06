# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Main for Train Calculator

from resources import Train, create_line, create_train, get_lines, get_trains
from math import sqrt

def main():
    choice = input("Do you want to \n(1) Create new trains \n(2) Create new lines \n(3) Create new trains and lines \n(4) Calculate \n")
    if choice == "1":
        create_train()
    elif choice == "2":
        create_line()
    elif choice == "3":
        create_train()
        create_line()


    print("Pick a train and a line to calculate the time. ")
    print("-----[THE TRAINS]-----")
    get_trains()
    choice_train = int(input("Train: ")) - 1
    with open("trains.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == choice_train:
                print(line)
                stats = line.split("/")
                train = Train(stats [0], stats [1], stats [2], stats [3])
    
    a = int(train.get_acceleration())
    v = int(train.get_speed())
    r = int(train.get_retardation())
    s0 = int((v**2)/(2*a))
    s1 = int((v**2)/(2*r))

    print("-----[THE LINES]-----")
    get_lines()
    choice_line = int(input("Line: ")) - 1
    with open("lines.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == choice_line:
                print(line)
                stats = line.split(",")

    x = 1
    name = stats[0]
    print(eval(name[1:]))
    for i in range(int((len(stats)-2)/2)):
        station = eval(stats[x])
        x += 1
        s = int(eval(stats[x]))
        x += 1
        if s < s0:
            time = sqrt(2 * s(1/a + 1/r))
        elif s > s0:
            time = v * (1/a + 1/r) + (s - s0 - s1)/v
        print(f"{station}")
        print(f"{round(time)} sekunder")
    end_station = stats[x]
    print(eval(end_station[:-1]))



    print(f"Acc = {a}m/s2 \nSpeed = {v}m/s \nRet = {r}m/s2 \nAcc Dist = {s0}m \nStop Dist = {s1}m")



if __name__ == "__main__":
    main()