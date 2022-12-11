from itertools import groupby
from string import ascii_lowercase, ascii_uppercase
from collections import namedtuple


EXAMPLE = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]

def figure_out_priority(item):
    priority = {}

    # Lowercase item types a through z have priorities 1 through 26.
    for index, letter in enumerate(ascii_lowercase):
        priority[letter] = index + 1

    # Uppercase item types A through Z have priorities 27 through 52.
    for index, letter in enumerate(ascii_uppercase):
        priority[letter] = index + 27

    return priority[item]


def part1():
    # bags = EXAMPLE

    with open('input.txt') as f:
        bags = f.read().splitlines()

    # found in both compartments
    found = []

    for bag in bags:
        middle_index = len(bag)//2
        first_half = bag[:middle_index]
        second_half = bag[middle_index:]
        for item in first_half:
            if item in second_half:
                found.append(item)
                break


    # Sum the priorities
    list_of_priorites = []
    for item in found:
        list_of_priorites.append(figure_out_priority(item))

    print(sum(list_of_priorites))

def part2():
    # bags = EXAMPLE

    with open('input.txt') as f:
        bags = f.read().splitlines()

    groups = []
    group = []
    i = 0
    for bag in bags:
        group.append(bag)
        i = i + 1
        if i == 3:
            groups.append(group)
            group = []
            i = 0


    # Better/Alternative way of grouping by n
    # n = 3
    # groups = [bags[i:i+n] for i in range(0, len(bags), n)]
    print(groups)

    found = []

    for group in groups:
        found.append(list(set(group[0]).intersection(group[1], group[2]))[0])

    # Sum the priorities
    list_of_priorites = []
    for item in found:
        list_of_priorites.append(figure_out_priority(item))

    print(sum(list_of_priorites))

if __name__ == "__main__":
    # part1()
    part2()
