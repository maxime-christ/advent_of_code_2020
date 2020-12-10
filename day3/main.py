#! /usr/bin/env python3

from array import array
from functools import reduce
import argparse

file = open('input.txt', 'r')
content = file.readlines()

def ex1(xstep, ystep: int):
    x, y, trees = 0, 0, 0
    height, width = content.__len__(), content[0].__len__()

    while y < height:
        if content[y][x] == '#':
            trees += 1
        x = (x+xstep)%(width-1)
        y+=ystep
    return trees

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('exercise')
    args = parser.parse_args()

    if args.exercise == 'ex1':
        print(ex1(3,1))
    elif args.exercise == 'ex2':
        print(reduce((lambda x,y: x*y), [ex1(1,1),ex1(3,1),ex1(5,1),ex1(7,1),ex1(1,2)]))
    else:
        raise Exception('Exercise unknown')
