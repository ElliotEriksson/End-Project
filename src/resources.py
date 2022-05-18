# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Resources for Train Calculator 

from time import sleep
from rich.progress import Progress

# Classes
class Train:

    def __init__(self, name : str, accelaration : int, speed : int, deceleration : int) -> None:
        """
        The constructor for the train class.

        Args:
            name (str): The name of the train.
            accelaration (int): The acceleration of the train.
            speed (int): The top speed of the train.
            deceleration (int): The deceleration of the train.
        """
        self.name = name
        self.acceleration = accelaration
        self.speed = speed
        self.deceleration = deceleration

    def get_name(self):
        return self.name

    def get_acceleration(self):
        return self.acceleration
    
    def get_speed(self):
        return self.speed

    def get_deceleration(self):
        return self.deceleration
        
    def save_train(self):
        return f"{self.name}/{self.acceleration}/{self.speed}/{self.deceleration}"

# Functions
def pro_bar():
    with Progress() as progress:
        task = progress.add_task("[red]Loading...", total=1000)
        while not progress.finished:
            progress.update(task, advance=20)
            sleep(0.01)


def create_train():
    """
    Create X amount of trains and append them to the trains.txt file.
    """
    trains = []
    amount = int(input("How many trains do you want to make? "))
    for i in range(amount):
        name = input("What is the name of the train? ")
        acc = int(input("What is the trains acceleration (m/s2)? "))
        speed = int(input("What is the trains top speed (m/s)? "))
        dec = int(input("What is the trains deceleration (m/s2)? "))
        all_stats = Train(name, acc, speed, dec)
        trains.append(all_stats.save_train())
    with open("trains.txt", "a", encoding="utf-8") as f:
        for list in trains:
            f.write('%s\n' % list)
    pro_bar()
    print("SUCCESS!  ")
   
def create_line():
    """
    Create X amount of lines and append them to the lines.txt file.
    """
    lines = []
    amount = int(input("How many train lines do you want to make? "))
    for i in range(amount):
        line = []
        name = input("What is the name of the line? ")
        line.append(name)
        station_amount = int(input("How many stations are there? "))
        last = 0
        for i in range(station_amount):
            distance = ""
            station_name = input("What is the name of the station? ")
            line.append(station_name)
            if last != station_amount - 1:
                distance = input("How far is it to the next station (m)? ")
                line.append(distance)
            last += 1
        lines.append(line)
    with open("lines.txt", "a", encoding="utf-8") as f:
        for list in lines:
            f.write('%s\n' % list)
    pro_bar()
    print("SUCCESS!  ")

def get_trains():
    """
    Prints all of the trains including their names and statistics.
    """
    pro_bar()
    print("-----[THE LINES]-----")
    number = 1
    with open("trains.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            print(f"({number}) {line.split('/')}")
            print()
            number += 1

def get_lines():
    """
    Prints all of the lines including their names, stations and distances.
    """
    pro_bar()
    print("-----[THE TRAINS]-----")
    number = 1
    with open("lines.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(f"({number}) {line}")
            number += 1
