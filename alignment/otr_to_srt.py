from pathlib import Path
import json
import re
from datetime import timedelta

import srt


class OtrToSrt:
    def __init__(self, infile):
        self.infile = infile
        self.raw = Path(infile).read_text(encoding='utf-8')
        self.parsed = None
        self.parse_raw()

    def parse_raw(self):
        content_json = json.loads(self.raw)
        raw = content_json['text']
        raw = raw.replace('<br />', '')
        raw = raw.split('</p>')

        # join everything that has no timestamp with following one
        turns = []
        i = 0
        in_turn = False
        while i < len(raw):
            # beginning
            if not turns:
                turns.append(raw[0])
                i += 1
                while not in_turn:
                    current = raw[i]
                    if 'timestamp' not in current:
                        turns[0] += raw[i]
                        i += 1
                    else:
                        turns[0] += current
                        in_turn = True
                        i += 1

            current = raw[i]
            if 'timestamp' not in current:
                turns[-1] += current
            else:
                turns.append(current)
            i += 1

        # clean turns
        for i, turn in enumerate(turns):
            # remove simplified timestamp
            turn = re.sub('>[0-9]{2}:[0-9]{2}<', '><', turn)
            # remove tags
            turn = turn.replace('<p>', '').replace('<span>', '').replace('</span>', '').replace('<span class="timestamp" data-timestamp="', '')
            turns[i] = turn

        # create pairs of timecode/transcript
        turns[0] = f'00.00000{turns[0].strip()}'

        for i, turn in enumerate(turns):
            pair = [t.strip() for t in turn.split('">')]
            turns[i] = pair

        # add ending timestamp
        def to_microseconds(time_str):
            return int(float(time_str) * 1000000)
        for i, turn in enumerate(turns):
            if i < len(turns)-1:
                end = turns[i+1][0]
            else:
                end = content_json['media-time']
            turns[i] = [to_microseconds(turn[0]), to_microseconds(end), turn[1]]

        self.parsed = turns

    def export_srt(self):
        subs = []
        idx = 1
        for start, end, turn in self.parsed:
            sub = srt.Subtitle(idx, start=timedelta(microseconds=start), end=timedelta(microseconds=end), content=turn)
            subs.append(sub)
            idx += 1
        srt_string = srt.compose(subs)
        out_file = self.infile.parent / (self.infile.stem + '.srt')
        out_file.write_text(srt_string)


#OtrToSrt(infile=Path('RR Shechen.otr')).export_srt()


for f in Path('./').glob('*.otr'):
    OtrToSrt(infile=f).export_srt()