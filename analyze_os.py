import csv
import operator

def main():
    total = 0
    amount_ubuntu = 0
    amount_windows = 0

    with open('os.csv') as myFile:
        reader = csv.reader(myFile)

        next(reader)

        sort = sorted(reader, key=operator.itemgetter(0))

        for _, row in enumerate(sort):
            for c, col in enumerate(row):
                if c == 2:
                    total += 1
                    if col.lower() == 'ubuntu':
                        amount_ubuntu += 1
                    elif col.lower() == 'windows':
                        amount_windows += 1

    print('\nResults:')
    print('Total Machines: %d' % (total))
    print('Ubuntu: %d Machines / %s' % (amount_ubuntu, "{:.2f}".format((amount_ubuntu / total) * 100) + '%'))
    print('Windows: %d Machines / %s' % (amount_windows, "{:.2f}".format((amount_windows / total) * 100) + '%'))

main()