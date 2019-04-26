import csv

def read_csv(filename):

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばしたい時

        return [[row[0], int(row[1]), row[2]] for row in reader]
