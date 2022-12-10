# DAY 1 - Calorie Counting

# Input - list of list of calories of each elf
# Each list in list needs to be totaled and then compared

from collections import namedtuple

EXAMPLE_LIST = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

def main():

    # Example list for testing
    # print(EXAMPLE_LIST)
    # calories_list = EXAMPLE_LIST
    # print(calories_list)

    # Get inputs into a list of lists
    with open('calorie_list.txt') as f:
        lines = f.read().splitlines()

    # Remove spaces
    lines = [line.replace(' ', '') for line in lines]

    # Create list of list
    calories_list = []
    sub_list = []
    for line in lines:
        if line == '':
            calories_list.append(sub_list)
            sub_list = []
        else:
            sub_list.append(int(line))

    elves = []
    # Create list of elves with their id and total carrying calories
    for calories in calories_list:
        elves.append(sum(calories))

    # Find the Elf with most calories
    most_calories = 0
    for elf in elves:
        if elf >= most_calories:
            most_calories = elf

    # Alternatice
    print(max(elves))

    print("*****************************************************************************")
    print(f"Elf with most calories: {most_calories} ")
    print(f"Elf with most calories: {max(elves)} ")
    print("*****************************************************************************")

    num_of_elves = len(elves)
    print(num_of_elves)

    elves.sort()

    sum_top_three = sum([elves[num_of_elves-1], elves[num_of_elves-2], elves[num_of_elves-3]])
    print(sum_top_three)

if __name__ == "__main__":
    main()