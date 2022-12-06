filename = './day6/data.txt'

def run():
    last4 = []
    last14 = []
    count = 1

    with open(filename) as fh:
        for line in fh:
            line = line.strip('\n')

            for char in line:

                last4.append(char)
                last14.append(char)

                if len(last4) == 5:
                    last4.pop(0)
                if len(last14) == 15:
                    last14.pop(0)

                last4check = set(last4)
                last14check = set(last14)

                print(f"Last 4 with Dupes: {last4} - {count}")
                print(f"Last 14 with Dupes: {last14} - {count}")

                if count >= 4 and len(last4check) == 4:
                    print(f"Found: {char} - Count: {count}")
                    # quit() # Uncomment out for part 1

                if count >= 14 and len(last14check) == 14:
                    print(f"Part 2 Found: {char} - Count: {count}")
                    quit()  # Comment for part 1

                count += 1
