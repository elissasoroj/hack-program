#!/usr/bin/env python

"""
Command line interface to sketch_prompt
"""

import argparse
from sketchprompt import subject, timelimit, scheme, color, timer


def parse_command_line():
    "parses args for the sketch_prompt funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--prompt",
        help="returns full prompt",
        action="store_true")

    # add long args
    parser.add_argument(
        "--subject", "-sub",
        help="returns random sketch subject",
        action="store_true")

    # add long args
    parser.add_argument(
        "--animal", "-a",
        help="returns a random animal subject",
        action="store_true")

    # add long args
    parser.add_argument(
        "--plant", "-p",
        help="returns a random plant subject",
        action="store_true")

    # add long args
    parser.add_argument(
        "--object", "-ho",
        help="returns a random household object",
        action="store_true")

    parser.add_argument(
        "--chordata", "--gbifa",
        help="returns a random animal species from GBIF",
        action="store_true")

    parser.add_argument(
        "--plantae", "--gbifp",
        help="returns a random plant species from GBIF",
        action="store_true")

    parser.add_argument(
        "--color", "-col",
        help="returns a hue",
        action="store_true")

    parser.add_argument(
        "--scheme",
        help="returns a color scheme",
        action="store_true")

    parser.add_argument(
        "--time",
        help="returns a random time limit",
        action="store_true")

    parser.add_argument(
        "t",
        type = int,
        nargs="?",
        help="time in seconds")

    parser.add_argument(
        "-c", "--clock",
        help="starts a coundown clock; use Ctrl+C to exit",
        action="store_true")

    # parse args
    args = parser.parse_args()

    # check that user only entered one action arg
    if sum([args.animal, args.plant, args.object, args.subject]) > 1:
        raise SystemExit(
            "only one 'subject' at a time.")
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call sketchprompt function
    if args.subject:
        print("----------- \nSubject:")
        subject("")
    elif args.animal:
        print("----------- \nSubject:")
        subject('animal')
    elif args.plant:
        print("----------- \nSubject:")
        subject('plant') 
    elif args.object:
        print("----------- \nSubject:")
        subject('object')
    elif args.chordata:
        print("----------- \nSubject:")
        subject('chordata')
    elif args.plantae:
        print("----------- \nSubject:")
        subject('plantae')

    if args.scheme:
        print("----------- \nColor Scheme:")
        scheme()

    if args.color:
        print("----------- \nColor:")
        color()

    if args.time:
        print("----------- \nTime Limit:")
        timelimit()

    if args.prompt:
        print("----------- \nFull Prompt:")
        subject("")
        scheme()
        color()
        timelimit()
        timer(timelimit.timetosec)

    if args.clock:
        print("----------- \nTimer:")
        timer(args.t)


if __name__ == "__main__":
    print("----------- \nFull Prompt:")
    subject("")
    colorscheme()
    color()
    timelimit()
    timer(timelimit.timetosec)

