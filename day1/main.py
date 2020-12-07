#! /usr/bin/env python3

from array import array
import argparse

def parse_input(file_name):
    input_file = open(file_name, 'r')
    values = array('I')
    line = input_file.readline()
    while line:
        values.append(int(line))
        line = input_file.readline()
    input_file.close()
    return sorted(values)

def ex1():
    values = parse_input('input.txt')
    first = 0
    last = values.__len__() - 1
    while True:
        s = values[first] + values[last]
        if s > 2020:
            last -= 1
        elif s < 2020:
            first += 1
        else: # s = 2020
            print(values[first] * values[last])
            return
        if first == last:
            raise Exception('No pair sums to 2020!')

def ex2():
    values = parse_input('input.txt')
    first = 0
    pivot = 1
    last = values.__len__() - 1
    while True:
        s = values[first] + values[pivot] + values[last]
        if s > 2020:
            last -= 1
        elif s < 2020:
            first += 1
        else:
            print(values[first] * values[pivot] * values[last])
            print(values[first])
            return
        if (first == pivot or pivot == last):
            first = 0
            pivot += 1
            last = values.__len__() - 1
        if pivot == values.__len__() - 1:
            raise Exception('No trio sums to 2020')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('exercise')
    args = parser.parse_args()

    if args.exercise == 'ex1':
        ex1()
    elif args.exercise == 'ex2':
        ex2()
    else:
        raise Exception('Exercise unknown')
