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
        help="starts a coundown clock",
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

    # pass argument to call darwinday function
    if args.subject:
        subject("")
    elif args.animal:
        subject('animal')
    elif args.plant:
        subject('plant')
    elif args.object:
        subject('object')
    elif args.chordata:
        subject('chordata')
    elif args.plantae:
        subject('plantae')

    if args.scheme:
        scheme()

    if args.color:
        color()

    if args.time:
        timelimit()

    if args.prompt:
        subject("")
        timelimit()
        scheme()
        color()
        timer(timelimit.timetosec)

    if args.clock:
        timer(args.t)


if __name__ == "__main__":
    subject("")
    timelimit()
    colorscheme()
    color()
    timer(timelimit.timetosec)

