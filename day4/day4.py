filename = './day4/data.txt'


def run():
    pairs = 0
    overlaps = 0
    with open(filename) as fh:
        for line in fh:
            print("=============")
            print(line)
            line = line.strip('\n')
            ranges = line.split(',')
            first = ranges[0].split('-')
            second = ranges[1].split('-')

            print(f"First: {first}")
            print(f"Second: {second}")

            first0 = int(first[0])
            first1 = int(first[1])
            second0 = int(second[0])
            second1 = int(second[1])

            if first0 >= second0 and first1 <= second1:
                pairs += 1
                print("PAIR")
            elif second0 >= first0 and second1 <= first1:
                pairs += 1
                print("PAIR")

            if second0 <= first0 <= second1:
                print("Overlap")
                overlaps += 1
            elif second0 <= first1 <= second1:
                print("Overlap")
                overlaps += 1
            elif first0 <= second0 <= first1:
                print("Overlap")
                overlaps += 1
            elif first0 <= second1 <= first1:
                print("Overlap")
                overlaps += 1

    print(f"Total Pairs: {pairs}")
    print(f"Total Overlaps: {overlaps}")
