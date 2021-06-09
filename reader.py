import csv
import operator
import json
import sys

from xlsxwriter.workbook import Workbook

def main():
    if (len(sys.argv) < 2):
        print("Not enough arguments supplied.\nUsage: python3 reader.py <file>.csv")
        return

    print(sys.argv)

    with open('users.json') as json_file:
        mapping = json.load(json_file)

    for i in range(1, len(sys.argv)):
        file_name = str(sys.argv[i])

        workbook = Workbook(file_name.split('.')[0] + '.xlsx')
        worksheet = workbook.add_worksheet()

        with open(sys.argv[i]) as myFile:
            reader = csv.reader(myFile)

            first_row = next(reader)
            worksheet.write(0, 0, 'Owner Name')
            for c, col in enumerate(first_row):
                worksheet.write(0, c + 1, col)

            sort = sorted(reader, key=operator.itemgetter(0))

            for r, row in enumerate(sort):
                for c, col in enumerate(row):
                    if (col[0:7].lower() == 'machine'):
                        for p in mapping['users']:
                            if (p['hostname'] == col):
                                worksheet.write(r + 1, 0, p['name'])

                    worksheet.write(r + 1, c + 1, col)

        workbook.close()

main()