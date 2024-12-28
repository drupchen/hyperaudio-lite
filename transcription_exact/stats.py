import csv
from pathlib import Path
import datetime


def gen_stats(in_file, threshold=10):
    with open(in_file, newline='') as csvfile:
        # A. parse file
        reader = csv.reader(csvfile, delimiter=',')
        distr = dict()

        line_num = 1
        for start, end, l, trans in reader:
            seconds = str(int(l) / 1000)
            s = seconds.split('.')[0]
            if len(s) == 1:
                s = '0'+s
            if s not in distr:
                distr[s] = {'count': 0, 'list': []}

            distr[s]['count'] += 1
            distr[s]['list'].append((start, trans, line_num))
            line_num += 1

        # B. format
        distr = sorted([(k, v) for k, v in distr.items()])

        summary = []
        output = []
        for secs, entry in distr:
            cat = f'\n{entry["count"]} strings of {secs}s:'
            summary.append(f'{entry["count"]} strings of {secs}s.')
            # add long strings to output
            if int(secs) >= threshold:
                output.append(cat)
                for start, string, l_num in entry['list']:
                    if string.strip():
                        output.append(f'\t{l_num} — {str(datetime.timedelta(milliseconds=int(start)))[:-3]} — "{string}"')

        output = '\n'.join(summary + output)

        # C. write
        in_file = Path(in_file)
        out = in_file.parent / f'stats_{in_file.stem}.txt'
        out.write_text(output)


if __name__ == '__main__':
    for f in Path().cwd().glob('*.csv'):
        gen_stats(f, 10)