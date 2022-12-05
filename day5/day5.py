filename = './day5/data.txt'

# crates = [[], [], []]
# crates[0] = ['N', 'Z']
# crates[1] = ['D', 'C', 'M']
# crates[2] = ['P']


# [S]                 [T] [Q]
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]

crates = [[], [], [], [],[],[],[],[], [], [], [], []]
crates[0] = ['S', 'L', 'F', 'Z', 'D', 'B', 'R', 'H']
crates[1] = ['R', 'Z', 'M', 'B', 'T']
crates[2] = ['S', 'N', ' H', 'C', 'L', 'Z']
crates[3] = ['J', 'F', 'C', 'S']
crates[4] = ['B', 'Z', 'R', 'W', 'H', 'G', 'P']
crates[5] = ['T', 'M', 'N', 'D', 'G', 'Z', 'J', 'V']
crates[6] = ['Q', 'P', 'S', 'F', 'W', 'N', 'L', 'G']
crates[7] = ['R', 'Z', 'M']
crates[8] = ['T', 'R', 'V', 'G', 'L', 'C', 'M']

def run():
    print(crates)
    with open(filename) as fh:
        for line in fh:
            line = line.strip('\n')

            print("============")
            print(line)

            split = line.split(' from ')
            move = int(split[0].split('move ').pop())
            split2 = split[1].split(' to ')
            to = int(split2.pop())
            from1 = int(split2.pop())

            crate = crates[from1 - 1]
            to_crate = crates[to - 1]

            print(f"Move {move}")
            move_count = move

            print(f"From:{crate}")
            print(f"To:{to_crate}")

            remove = []
            add = []

            for x in crate:
                index = crate.index(x)
                if move_count > 0:
                    print(f"Char: {x}")
                    move_count -= 1
                    remove.append(x)
                    # to_crate.insert(0, x)
                    add.append(x)
                    # to_crate.append(x)

            for x in remove:
                crate.remove(x)

            print(f"Adding {add}")

            add.reverse()

            for x in add:
                to_crate.insert(0, x)

                # if move_count > 0:

                #     print(f"Moving {x} to {to} - move count {move_count}")
                #     move_count -= 1

            to_crate = crates[to - 1]

            print(f"Result: {to_crate}")
            print("============")
            # input("Next?")

    popped = []
    for x in crates:
        print(f"Crate: {x}")
        for i in x:

            if i.isalpha():
                print(f"Item: {i}")
                popped.append(i)
                break

    print(crates)
    print(f"Popped: {''.join(popped)}")
