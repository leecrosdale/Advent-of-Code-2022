filename = './day1/data.txt'
def run():
    print("DAY 1")
    amount = 0
    amounts = []

    with open(filename) as fh:
        for line in fh:
            if line != '\n':
                amount = amount + int(line)
            else:
                amounts.append(amount)
                amount = 0

    highest_number = max(amounts)
    print("Highest Number: " + str(highest_number))
    top3total = sum(sorted(amounts, reverse=True)[0:3])
    print("Total 3 total: " + str(top3total))