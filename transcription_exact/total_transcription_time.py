import csv
from pathlib import Path
import datetime

from collections import defaultdict


if __name__ == '__main__':
    total = 0
    per_file = defaultdict(int)
    for f in Path().cwd().glob('*.csv'):
        with open(f, newline='') as csvfile:
            name = f.stem
            # A. parse file
            reader = csv.reader(csvfile, delimiter=',')
            distr = dict()

            for start, end, l, trans in reader:
                l = int(l)
                total += l
                per_file[name] += l

    total = str(datetime.timedelta(milliseconds=int(total)))[:-3]
    for k, v in per_file.items():
        per_file[k] = str(datetime.timedelta(milliseconds=int(v)))[:-3]

    out = []
    out.append(f'total amount of data: {total}\n')
    for k in sorted(per_file.keys()):
        out.append(f'{k}: {per_file[k]}')
    Path('total_training_data.txt').write_text('\n'.join(out))