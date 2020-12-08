#! /usr/bin/env python3

import re
from array import array
import argparse

def main(ex:str):
    file = open('input.txt', 'r')
    line = file.readline()
    policy_regex = re.compile('\d+-\d+ [a-z]:')
    occur_regex = re.compile('\d+')
    char_regex = re.compile('[a-z]')
    count = 0
    while line:
        policy = policy_regex.match(line)
        if not policy:
            raise Exception('Unknown policy format')
        pwd = line[policy.end() + 1:-1]
        occur = occur_regex.findall(policy.group())
        char_to_match = char_regex.search(policy.group()).group()
        pwd_char_occur = re.findall(char_to_match, pwd)

        if ex == 'ex1':
            if (pwd_char_occur.__len__() >= int(occur[0]) and pwd_char_occur.__len__() <= int(occur[1])):
                count += 1
        elif ex == 'ex2':
            if int(occur[1])-1 >= pwd.__len__():
                line = file.readline()
                continue
            s = pwd[int(occur[0])-1] + pwd[int(occur[1])-1]
            if re.findall(char_to_match, s).__len__() == 1:
                count += 1
        else:
            raise Exception('Exrcise unknown!')

        line = file.readline()
    print(count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('exercise')
    args = parser.parse_args()
    main(args.exercise)
