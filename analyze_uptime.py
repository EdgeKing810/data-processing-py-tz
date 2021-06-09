import csv
import operator
import json
import sys

def main():
    total_machines = 0
    total_uptime = 0
    average_uptime = 0
    max_uptime = -1
    max_uptime_user = ''

    with open('users.json') as json_file:
        mapping = json.load(json_file)

    with open('uptime.csv') as myFile:
        reader = csv.reader(myFile)

        next(reader)

        sort = sorted(reader, key=operator.itemgetter(0))

        for _, row in enumerate(sort):
            for c, col in enumerate(row):
                if c == 1:
                    total_machines += 1
                    total_uptime += int(col)
                    if int(col) > max_uptime:
                        max_uptime = int(col)
                        for p in mapping['users']:
                            if (p['hostname'] == row[0]):
                                max_uptime_user = p['name']

    average_uptime = "{:.2f}".format(total_uptime / total_machines);

    print('\nResults:')
    print('Total Uptime: %d days' % (total_uptime))
    print('Average Uptime: %s days' % (average_uptime))
    print('%s has the highest uptime with %d days' % (max_uptime_user, max_uptime))

main()