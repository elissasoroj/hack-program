#!/usr/bin/env python

"""
A function that generates a random sketch prompt with options:
1. subject
2. time limit
3. color scheme
4. main hue (color)

Also provides a countdown timer

"""
import os
import time
import playsound
import keyboard
import pandas as pd
import numpy as np
import rich

here = os.path.dirname(os.path.abspath(__file__))

def func():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "data_subdir", "binfile.dat"), "rb") as f:
        data = f.read()
    with open(os.path.join(here, "data_subdir", "textfile.txt"), "rt") as f:
        text = f.read()

# Read in data lists
master = pd.read_csv(os.path.join(here, "lists", "master.csv"))

#Define variables
timeout = []
timetosec = {}
colout = []
coldisplay = []

#Define masks
allsub = master['type'] == 'subject'
animals = master['category'] == 'animal'
plants = master['category'] == 'plant'
objects = master['category'] == 'household object'
colors = master['type'] == 'color'
schemes = master['type'] == 'scheme'
limits = master['type'] == 'limits'


def subject(arg):
    "returns a subject"

    if arg == "plantae":
        plantae_raw = pd.read_csv(os.path.join(here, "lists", "plantae.csv"))
        plantae = plantae_raw['species']
        print(plantae.sample().to_string(index=False).strip())

    elif arg == "chordata":
        chordata_raw = pd.read_csv(os.path.join(here, "lists", "chordata.csv"))
        chordata = chordata_raw['species']
        print(chordata.sample().to_string(index=False).strip())

    elif arg == "animal":
        print(master.loc[animals]['data'].sample().to_string(index=False).strip())

    elif arg == "plant":
        print(master.loc[plants]['data'].sample().to_string(index=False).strip())

    elif arg == "object":
        print(master.loc[objects]['data'].sample().to_string(index=False).strip())

    else:
        print(master.loc[allsub]['data'].sample().to_string(index=False).strip())



def timelimit():
    "returns a time limit"
    timelimit.timeout = master.loc[master['type'] == 'limit']['data'].sample()
    timelimit.timetosec = int(timelimit.timeout)*60
    print(" time limit:", timelimit.timeout.to_string(index=False), "minute(s)")
    

def scheme():
    "returns a color scheme"
    print(master.loc[schemes]['data'].sample().to_string(index=False).strip())

def color():
    "returns a main color for the color scheme"
    #print(master.loc[colors]['data'].sample().to_string(index=False))
    from rich import print as rprint
    from rich import color
    color.colout = master.loc[colors]['data'].sample().to_string(index=False).strip()
    color.colalt = master.loc[master['data'] == color.colout]['alttext'].to_string(index=False).strip()
    rprint(color.colalt, f":[default on {color.colout}]                 [/]")

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
    try:
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
        print("Time's Up!\n\n")
        from playsound import playsound
        playsound(os.path.join(here, "mallet.mp3"))
        
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    subject("")
    timelimit()
    scheme()
    color()
    timer(timelimit.timetosec)