# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Main for Train Calculator

from xmlrpc.client import FastParser
from resources import Train, create_line, create_train, get_lines, get_trains
from math import sqrt


def main():
    choice = input("Do you want to \n(1) Create new lines \n(2) Create new trains \n(3) Create new trains and lines \n(4) Calculate / Compare \n")
    if choice == "1":
        create_line()
    elif choice == "2":
        create_train()
    elif choice == "3":
        create_train()
        create_line()    
    elif choice == "4":
        choice = input("Do you want to (1) Compare 1 or more trains across a single line or (2) Compare 1 train across different lines? ")
        print("-----[THE LINES]-----")
        get_lines()
        print()
        print("-----[THE TRAINS]-----")
        get_trains()
        # Comparing MULTIPLE trains across ONE line
        if choice == "1":
            names = []
            list_total = []
            choice_line = int(input("Pick a line: ")) - 1
            with open("lines.txt", "r", encoding="utf-8") as f:
                for i, line in enumerate(f):
                    if i == choice_line:
                        stats = line.split(",")
            amount = int(input("How many trains do you want to compare (1 if you just want to calculate for a single train)? "))
            train_number = 1
            for i in range(amount):
                choice_train = int(input(f"Train nr{train_number}: ")) - 1
                train_number += 1
                with open("trains.txt", "r", encoding="utf-8") as f:
                    for i, line in enumerate(f):
                        if i == choice_train:
                            attr = line.split("/")
                            train = Train(attr[0], attr[1], attr[2], attr[3])
                            names.append(attr[0])
                # Assigning values to the different units
                a = float(train.get_acceleration())
                v = float(train.get_speed())
                r = float(train.get_retardation())
                s0 = int((v**2)/(2*a))
                s1 = int((v**2)/(2*r))

                # Calculating the time it takes and printing it out.
                x = 1
                total_time = 0
                print(eval(stats[0][1:]))
                for i in range(int((len(stats)-2)/2)):
                    station = eval(stats[x])
                    x += 1
                    s = int(eval(stats[x]))
                    x += 1
                    if s < s0:
                        time = sqrt(2 * s(1/a + 1/r))
                    elif s > s0:
                        time = v * (1/a + 1/r) + (s - s0 - s1)/v
                    total_time += time
                    print(f"{station}")
                    print(f"{round(time)} seconds")
                list_total.append(round(total_time))
                print(eval(stats[x][:-1]))
                print(f"It takes a total of {round(total_time)} seconds to travel across {eval(stats[0] [1:])} with the {attr[0]}.")
                print()
            
            # Printing out the fastest and slowest trains and the difference between them
            fastest = names[list_total.index(min(list_total))]
            slowest = names[list_total.index(max(list_total))]
            if amount > 1:
                print(f"{fastest} is the fastest and takes {min(list_total)} seconds.")
                print(f"{slowest} is the slowest and takes {max(list_total)} seconds")
                print(f"{fastest} is {max(list_total) - min(list_total)} seconds faster than {slowest}")

        choice = input("Do you want to restart the program (y/n)? ")
        if choice == "y":
            main()
        else:
            print("Thank you for using the program.")
            quit()
    else:
        print(f"{choice} is not an answer. Try again")
        main()
    
if __name__ == "__main__":
    main()