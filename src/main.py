# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Main for Train Calculator



import time
from resources import Train, create_line, create_train, get_lines, get_trains
from math import sqrt



def end_program():
    valid = False
    choice = input("Do you want to restart the program (y/n)? ")
    while not valid:
        if choice == "y":
            main()
        elif choice == "n":
            print("Thank you for using the program.")
            valid = True
        else:
            print(f"{choice} is not an acceptable answer.")
            print()

def main():
    list_total = []
    valid = False
    # Count to amount of lines in "lines.txt"
    with open("lines.txt", "r", encoding="utf-8") as f:
        for count, line in enumerate(f):
            pass

    while not valid:
        choice = input("Do you want to \n(1) Create new lines \n(2) Create new trains \n(3) Create new trains and lines \n(4) Calculate / Compare \n(5) Exit the program\n")
        if choice == "1":
            create_line()

        elif choice == "2":
            create_train()

        elif choice == "3":
            create_train()
            create_line()    

        elif choice == "4":
            print("-----[THE LINES]-----")
            get_lines()
            print()
            print("-----[THE TRAINS]-----")
            get_trains()
            while not valid:
                choice = input("Do you want to (1) Compare one or more trains across a single line or (2) Compare one train across multiple lines? ")

                # Comparing MULTIPLE trains across ONE line
                if choice == "1":
                    names = []
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
                        # Assigning values to the different units
                        names.append(train.get_name())
                        a = float(train.get_acceleration())
                        v = float(train.get_speed())
                        r = float(train.get_retardation())
                        s0 = int((v**2)/(2*a))
                        s1 = int((v**2)/(2*r))

                        # Calculating the time it takes and printing it out.
                        print(eval(stats[0][1:]))
                        x = 1
                        total_time = 0
                        for i in range(int((len(stats)-2)/2)):
                            station = eval(stats[x])
                            x += 1
                            s = int(eval(stats[x]))
                            x += 1
                            if s < s0:
                                sec = sqrt(2 * s * (1/a + 1/r))
                            elif s > s0:
                                sec = v * (1/a + 1/r) + (s - s0 - s1)/v
                            print(f"{station}")
                            time.sleep(0.7)
                            print(f"{round(sec)} seconds")
                            total_time += sec
                        list_total.append(round(total_time))
                        if count == choice_line:
                            print(eval(stats[x][:-1]))
                        else:
                            print(eval(stats[x][:-2]))                            
                        print(f"It takes a total of {round(total_time)} seconds to travel across {eval(stats[0] [1:])} with the {attr[0]}.")
                        print("This does not include stoppage time at the stations")
                        print()

                    # Printing out the fastest and slowest trains and the difference between them            
                    if amount > 1:
                        fastest = names[list_total.index(min(list_total))]
                        slowest = names[list_total.index(max(list_total))]
                        print(f"{fastest} is the fastest and takes {min(list_total)} seconds.")
                        print(f"{slowest} is the slowest and takes {max(list_total)} seconds.")
                        print(f"{fastest} is {max(list_total) - min(list_total)} seconds faster than {slowest}.")
                    valid = True

                # Comparing ONE train across MULTIPLE lines
                elif choice == "2":
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
                    line_number = 1
                    lines = [[] for i in range(amount)]
                    for i in range(amount):
                        choice_line = int(input(f"Line nr{line_number}: ")) - 1
                        line_number += 1
                        with open("lines.txt", "r", encoding="utf-8") as f:
                            for y, line in enumerate(f):
                                if y == choice_line:
                                    stats = line.split(",")
                                    lines[z].append(stats[0][1:])
                                    x = 1
                                    for i in range(int(len(stats)-2)):
                                        lines[z].append(eval(stats[x]))
                                        x += 1
                                    if count == choice_line:
                                        lines[z].append(eval(stats[x][:-1]))
                                    else:
                                        lines[z].append(eval(stats[x][:-2]))
                            
                            # Calculating the time it takes and printing it out.
                            print(eval(lines[z][0]))
                            x = 1
                            total_time = 0
                            for i in range(int((len(lines[z])-2)/2)):
                                station = (lines[z][x])
                                x += 1
                                s = int(lines[z][x])
                                x += 1
                                if s < s0:
                                    sec = sqrt(2 * s * (1/a + 1/r))
                                elif s > s0:
                                    sec = v * (1/a + 1/r) + (s - s0 - s1)/v
                                print(station)
                                time.sleep(.7)
                                print(f"{round(sec)} seconds")
                                total_time += sec
                            list_total.append(round(total_time))
                            print(lines[z][x])
                            print(f"It takes a total of {round(total_time)} seconds to travel across {eval(lines[z][0])} with the {attr[0]}.")
                            print("This does not include stoppage time at the stations.")
                            print()
                            z += 1

                    # Printing out the short and longest line and the difference between them.
                    if amount > 1:
                        shortest = lines[list_total.index(min(list_total))][0]
                        longest = lines[list_total.index(max(list_total))][0]
                        print(f"{shortest} is the shortest and takes {min(list_total)} seconds.")
                        print(f"{longest} is the longest and takes {max(list_total)} seconds.")
                        print(f"{shortest} takes {max(list_total) - min(list_total)} seconds less than {longest}.")
                        print()
                    valid = True
                    
                else:
                    print(f"{choice} is not a acceptable answer.")
                    print()

            end_program()

        elif choice == "5":
            print("Thank you for using the program.")
            valid = True

        else:
            print(f"{choice} is not an answer. Please try again.")
            print()
    
if __name__ == "__main__":
    main()