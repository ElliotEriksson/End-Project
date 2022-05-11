# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Main for Train Calculator

from time import sleep
from resources import Train, create_line, create_train, get_lines, get_trains
from math import sqrt
from rich.console import Console
from rich.style import Style
console = Console()


def main():
    valid = False
    list_total = []
    count_line = -1
    count_train = -1
    # Counting the amount of trains / lines in the txt files.
    with open("lines.txt", "r", encoding="utf-8") as f:
        for line in f:
            count_line += 1
    with open("trains.txt", "r", encoding="utf-8") as f:
        for line in f:
            count_train += 1
    while not valid:
        choice = input("Do you want to \n(1) Create new lines \n(2) Create new trains \n(3) Create new trains and lines \n(4) Calculate / Compare \n(5) Exit the program\n")
        if choice == "1":
            create_line()
        elif choice == "2":
            create_train()
        elif choice == "3":
            create_line()  
            create_train()  
        elif choice == "4":
            while not valid:
                choice = input("Do you want to (1) Compare one or more trains across a single line or (2) Compare one train across multiple lines? ")
                
                # Comparing MULTIPLE trains across ONE line.
                if choice == "1":
                    names = []
                    # Choosing the line.
                    while not valid:
                        get_lines()
                        choice_line = int(input("Pick a line: ")) - 1
                        if choice_line <= count_line:
                            with open("lines.txt", "r", encoding="utf-8") as f:
                                for i, line in enumerate(f):
                                    if i == choice_line:
                                        stats = line.split(",")
                            # Choosing the train(s)
                            while not valid:
                                amount = int(input("How many trains do you want to compare (1 if you just want to calculate for a single train)? "))
                                if amount - 1 <= count_train:
                                    train_number = 1
                                    for i in range(amount):
                                        while not valid:
                                            get_trains()
                                            choice_train = int(input(f"Train nr{train_number}: ")) - 1
                                            if choice_train <= count_train:
                                                train_number += 1
                                                with open("trains.txt", "r", encoding="utf-8") as f:
                                                    for i, line in enumerate(f):
                                                        if i == choice_train:
                                                            attr = line.split("/")
                                                            train = Train(attr[0], attr[1], attr[2], attr[3])
                                                # Assigning values to the different units.
                                                names.append(train.get_name())
                                                a = float(train.get_acceleration())
                                                v = float(train.get_speed())
                                                r = float(train.get_deceleration())
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
                                                    sleep(0.7)
                                                    print(f"{round(sec)} seconds")
                                                    total_time += sec
                                                list_total.append(round(total_time))
                                                print(eval(stats[x][:-2]))                            
                                                print(f"It takes a total of {round(total_time)} seconds to travel across {eval(stats[0] [1:])} with the {attr[0]}.")
                                                print("This does not include stoppage time at the stations.")
                                                print()
                                                if amount == train_number - 1:
                                                    valid = True
                                            else:
                                                print(f"{choice_train + 1} is not an acceptable answer.")
                                                print("Try again.")

                                    # Printing out the fastest and slowest trains and the difference between them.
                                    if amount > 1:
                                        fastest = names[list_total.index(min(list_total))]
                                        slowest = names[list_total.index(max(list_total))]
                                        console.print(f"{fastest} is the fastest and takes {min(list_total)} seconds.", style = Style(color="green"))
                                        console.print(f"{slowest} is the slowest and takes {max(list_total)} seconds.", style = Style(color="red"))
                                        print(f"The fastest train ({fastest}) is {max(list_total) - min(list_total)} seconds faster than the slowest train ({slowest}).")
                                        print()
                                    valid = True
                                else:
                                    print(f"{amount} is more than the amount of trains.")
                                    print("Try again.")

                        else:
                            print(f"{choice_line + 1} is not a valid answer")
                            print("Try again.")

                    
                # Comparing ONE train across MULTIPLE lines.
                elif choice == "2":
                    # Choosing the train
                    while not valid:
                        choice_train = int(input("Pick your train: ")) - 1
                        if choice_train <= count_train:
                            with open("trains.txt", "r", encoding="utf-8") as f:
                                for i, line in enumerate(f):
                                    if i == choice_train:
                                        attr = line.split("/")
                                        train = Train(attr[0], attr[1], attr[2], attr[3])
                            # Assigning values to the different units.
                            a = float(train.get_acceleration())
                            v = float(train.get_speed())
                            r = float(train.get_deceleration())
                            s0 = int((v**2)/(2*a))
                            s1 = int((v**2)/(2*r))

                            # Choosing the line(s)
                            while not valid:
                                amount = int(input("How many lines do you want to compare (1 if you just want to calculate for a single line)? "))
                                if amount - 1 <= count_line:
                                    z = 0
                                    line_number = 1
                                    lines = [[] for i in range(amount)]
                                    for i in range(amount):
                                        while not valid:
                                            get_lines()
                                            choice_line = int(input(f"Line nr{line_number}: ")) - 1
                                            if choice_line <= count_line:
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
                                                        sleep(.7)
                                                        print(f"{round(sec)} seconds")
                                                        total_time += sec
                                                    list_total.append(round(total_time))
                                                    print(lines[z][x])
                                                    print(f"It takes a total of {round(total_time)} seconds to travel across {eval(lines[z][0])} with the {attr[0]}.")
                                                    print("This does not include stoppage time at the stations.")
                                                    print()
                                                    z += 1
                                                    if amount == line_number -1:
                                                        valid = True
                                            else:
                                                print(f"{choice_line + 1} is not a acceptable answer.")
                                                print()

                                    # Printing out the short and longest line and the difference between them.
                                    if amount > 1:
                                        shortest = eval(lines[list_total.index(min(list_total))][0])
                                        longest = eval(lines[list_total.index(max(list_total))][0])
                                        console.print(f"{shortest} is the shortest and takes {min(list_total)} seconds.", style = Style(color="green"))
                                        console.print(f"{longest} is the longest and takes {max(list_total)} seconds.", style = Style(color="red"))
                                        print(f"The shortest line ({shortest}) takes {max(list_total) - min(list_total)} seconds less than the longest line ({longest}).")
                                        print()
                                    valid = True
                                else:
                                    print(f"{amount} is not a acceptable answer.")
                                    print()   
                        else:
                            print(f"{choice_train + 1} is not a acceptable answer.")
                            print()    
                else:
                    print(f"{choice} is not a acceptable answer.")
                    print()
                    
            valid = False
            while not valid:
                choice = input("Do you want to restart the program (y/n)? ")
                if choice.lower() == "y":
                    print("yo")
                    main()
                elif choice.lower() == "n":
                    print("Thank you for using the program.")
                    quit()
                else:
                    print(f"{choice} is not an acceptable answer.")
                    print()


        elif choice == "5":
            print("Thank you for using the program.")
            quit()

        else:
            print(f"{choice} is not an answer. Please try again.")
            print()

if __name__ == "__main__":
    main()