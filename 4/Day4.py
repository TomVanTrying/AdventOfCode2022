def part1(input):
    counter = 0
    for line in input:
        # print("###########################")
        elf_pair = line.split(',')
        compare_pair = []
        for elf in elf_pair:
            start, end = elf.split('-')
            # print(f"{int(start)} {int(end)}")
            compare_pair.append(list(range(int(start), int(end)+1)))
        # print(compare_pair)

        if len(compare_pair[0]) >= len(compare_pair[1]):
            found = all(item in compare_pair[0] for item in compare_pair[1])
        else:
            found = all(item in compare_pair[1] for item in compare_pair[0])

        if found:
            counter = counter + 1

    print(f"XXXX {counter} XXXX")

def part2(input):
    counter = 0
    for line in input:
        # print("###########################")
        elf_pair = line.split(',')
        compare_pair = []
        for elf in elf_pair:
            start, end = elf.split('-')
            # print(f"{int(start)} {int(end)}")
            compare_pair.append(list(range(int(start), int(end)+1)))
        # print(compare_pair)

        if len(compare_pair[0]) >= len(compare_pair[1]):
            found = any(item in compare_pair[0] for item in compare_pair[1])
        else:
            found = any(item in compare_pair[1] for item in compare_pair[0])

        if found:
            counter = counter + 1

    print(f"XXXX {counter} XXXX")


if __name__ == "__main__":
    input = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8',
    ]

    part1(input)
    part2(input)

    with open('input.txt') as f:
        input = f.read().splitlines()

    part1(input)
    part2(input)


