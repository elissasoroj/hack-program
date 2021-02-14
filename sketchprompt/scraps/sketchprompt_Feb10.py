#!/usr/bin/env python

"""
A function that generates a random sketch prompt with options:
1. subject
2. time limit
3. color scheme
4. main hue (color)

Also provides a countdown timer

"""
import csv
import os
import random
import time
import playsound

here = os.path.dirname(os.path.abspath(__file__))

def func():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "data_subdir", "binfile.dat"), "rb") as f:
        data = f.read()
    with open(os.path.join(here, "data_subdir", "textfile.txt"), "rt") as f:
        text = f.read()

# Read in lists
with open(os.path.join(here, "lists", "animals.csv"), newline='', encoding='utf-8-sig') as f1:
        reader1 = csv.reader(f1)
        animals = list(reader1)

with open(os.path.join(here, "lists", "plants.csv"), newline='', encoding='utf-8-sig') as f2:
        reader2 = csv.reader(f2)
        plants = list(reader2)

with open(os.path.join(here, "lists", "objects.csv"), newline='', encoding='utf-8-sig') as f3:
        reader3 = csv.reader(f3)
        objects = list(reader3)

with open(os.path.join(here, "lists", "limits.csv"), newline='', encoding='utf-8-sig') as f4:
        reader4 = csv.reader(f4)
        limits = list(reader4)

with open(os.path.join(here, "lists", "schemes.csv"), newline='', encoding='utf-8-sig') as f5:
        reader5 = csv.reader(f5)
        schemes = list(reader5)

with open(os.path.join(here, "lists", "colors.csv"), newline='', encoding='utf-8-sig') as f6:
        reader6 = csv.reader(f6)
        colors = list(reader6)

#Define variables
ALLSUB = [animals, plants, objects]
timeout = []
timetosec = {}


def subject(arg):
    "returns a subject"

    if arg == "animal":
        print(random.choice(animals))

    elif arg == "plant":
        print(random.choice(plants))

    elif arg == "object":
        print(random.choice(objects))

    else:
        rand = random.choice(ALLSUB)
        print("subject:", *random.choice(rand))



def timelimit():
    "returns a time limit"
    timelimit.timeout = random.choice(limits)
    timelimit.timetosec = int(timelimit.timeout[0])*60
    print("time limit:", timelimit.timeout[0], "minute(s)")
    

def scheme():
    "returns a color scheme"
    print("color scheme:", *random.choice(schemes))

def color():
    "returns a main color for the color scheme"
    print("main hue:", *random.choice(colors))  

def timer(t):
    """
    starts a countdown timer; enter time in seconds:
    1 min = 60
    5 min = 300
    10 min = 600
    15 min = 900
    30 min = 1800
    1 hr = 3600
    ---
    Timer requires PyObjC  and playsound modules
    pip3 install -U PyObjC
    pip3 install playsound
    """
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    from playsound import playsound
    playsound(os.path.join(here, "mallet.mp3"))
    print("Time's Up!\n\n\n\n\n")


if __name__ == "__main__":
    subject("")
    timelimit()
    colorscheme()
    color()
    timer(timelimit.timetosec)

    ~code/git/hacks/hack-program/sketchprompt/mallet.mp3