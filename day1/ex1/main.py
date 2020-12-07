#! /usr/bin/env python3

from array import array

def parse_input(file_name):
    input_file = open(file_name, 'r')
    values = array('I')
    line = input_file.readline()
    while line:
        values.append(int(line))
        line = input_file.readline()
    input_file.close()
    return sorted(values)

def main():
    values = parse_input('input.txt')
    first = 0
    last = values.__len__() - 1
    i = 0
    while True:
        i+=1
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

if __name__ == "__main__":
    main()
