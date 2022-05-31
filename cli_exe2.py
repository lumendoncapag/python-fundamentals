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

def name_and_type_find(start,args):
    name = f"{start}/{args.name}"
    for f in start.rglob('*'):
        if (str(name)==str(f)):
            if args.type == "d" and f.is_dir():
                print(f)
            elif args.type == "f" and f.is_file():
                print(f)


def find(args):
    start = Path(args.start)

    if args.name and not args.type:
        name_find(start, args)
    elif args.type and not args.name:
        type_find(start,args)
    elif args.name!=None and args.type!=None:
        name_and_type_find(start,args)


#/home/lumendonca/Desktop/python-fundamentals/arquivo.txt
#/home/lumendonca/Desktop/python-fundamentals/arquivo.txt

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', type=str,required=False, help='Informa o dirétorio incial de procura')
    parser.add_argument('--name', type=str,help='Insira o nome do Arquivo ou Diretório a ser procurado')
    parser.add_argument('--type', type=str, choices=['d', 'f'],help='Selecione o tipo de arquivo: \n d - Diretório \n f - File')

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    validate_args(parser, args)
    find(args)


if __name__ == '__main__':
    main()
