filename = './day3/data.txt'


def run():
    total_value = 0
    backpack = 0
    elves_in_group = 2
    group = 0
    backpacks = ['', '', '']
    total_group_value = 0

    with open(filename) as fh:
        for line in fh:
            length = len(line)

            line = line.strip('\n')

            print("-----------------------------")
            print(f"Backpack: {line}")
            print(f"Length: {length}")

            half = length // 2

            compartment1 = slice(0, half)
            compartment2 = slice(half, length)

            first_half = line[compartment1]
            second_half = line[compartment2]

            match = set(first_half).intersection(second_half).pop()

            print(f"First Half: {first_half}")
            print(f"Second Half: {second_half}")

            value = alphabetLetter(match)

            print(f"Value: {value}")

            total_value = total_value + value

            backpacks[backpack] = line

            if backpack < elves_in_group:
                print(f"Backpack Number: {backpack}")
                backpack += 1
            else:
                print(f"Group {group} Backpacks: {backpacks}")
                backpack_match = set(backpacks[0]).intersection(backpacks[1], backpacks[2]).pop()
                print(f"Backpack Matches: {backpack_match}")
                group_value = alphabetLetter(backpack_match)
                total_group_value += group_value
                print(f"Group Value: {group_value}")
                backpack = 0
                backpacks = ['', '', '']
                group += 1

    print(f"=======RESULTS=======")
    print(f"Total Value: {total_value}")
    print(f"Total Group Value: {total_group_value}")


def alphabetLetter(letter):
    print(f"Letter: {letter}")

    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - ord('a') + 1
