from pathlib import Path

import srt




all_srt = (Path().cwd() / '..' / 'components').glob('*.srt')
all_srt = list(all_srt)

for s in all_srt:
    # parse srt
    dump = s.read_text()
    cur_srt = list(srt.parse(dump))
    data = []
    for sub in cur_srt:
        start = sub.start.total_seconds()*1000
        start = int(start)
        end = sub.end.total_seconds()*1000
        end = int(end)
        duration = end - start
        content = sub.content
        data.append((start,end,duration,content))

    # create csv
    out_file = Path().cwd() / (s.stem + '.csv')
    out = '\n'.join([f'{d[0]},{d[1]},{d[2]},"{d[3]}"' for d in data])
    out_file.write_text(out)
