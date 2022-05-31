#!/usr/bin/python3
import sys
import os
from pathlib import Path
import argparse

def validate_args(parser, args):
    if args.start == None:
        args.start = os.getcwd()
    if not os.path.isdir(args.start):
        parser.error('argument --start: O argumento de --start deve ser um caminho existente no sistema')


def name_find(start, args):
    for f in start.rglob(args.name):
        print(f)


def type_find(start, args):

    for f in start.rglob('*'):
        if args.type == "d" and f.is_dir():
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)


def find(args):
    start = Path(args.start)

    if args.name and not args.type:
        print(args.name)
        name_find(start, args)
    elif args.type and not args.name:
        type_find(start,args)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', type=str,required=False)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--name', type=str)
    group.add_argument('--type', type=str, choices=['d', 'f'])

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    validate_args(parser, args)
    print(args)
    find(args)


if __name__ == '__main__':
    main()
