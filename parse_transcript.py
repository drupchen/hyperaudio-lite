from pathlib import Path
import re

import srt

from components.html_parts import *


def parse_srt(in_file):
    """
    :param in_file: .srt utf-8 file
    :return: [{'start': <start-time-in-milliseconds>, 'end': <end-time-in-milliseconds>, 'content': <string>}, ...]
    """
    def to_milli(time):
        return int(time.total_seconds()*1000)

    raw = Path(in_file).read_text()
    sub_raw = list(srt.parse(raw))

    parsed = []
    for sub in sub_raw:
        start = to_milli(sub.start)
        end = to_milli(sub.end)
        content = sub.content
        content = normalize_punct(content)
        s = {'start': start, 'end': end, 'content': content}
        parsed.append(s)
    return parsed


def normalize_punct(string):
    string = string.strip().replace('་ ', '་')
    if string.endswith(' །'):
        pass
    elif string.endswith('།') or string.endswith('ཿ'):
        string += ' '
    return string


def gen_ha_page(in_file):
    # A. parse and prepare chunks
    parsed = parse_srt(in_file)
    chunks = []
    cur = []
    slide_num = []
    for p in parsed:
        if p['content'].startswith('{'):
            # add to chunks
            if cur:
                num = []
                if slide_num:
                    num = slide_num
                chunks.append((num, cur))
                cur = []
                slide_num = []

            # start new chunk
            text = p['content']
            while '}' in text:
                s_num, text = text.split('}', 1)
                slide_num.append(int(s_num[1:]))
            p['content'] = text
            cur.append(p)
        else:
            cur.append(p)
    # trailing chunk
    if cur:
        chunks.append((slide_num, cur))

    # B. format and add ha html code
    ha_trans = []
    for s_num, chunk in chunks:
        # add slide to html
        if s_num:
            for n, s in enumerate(s_num):
                img = f'\n<img src="components/slides/slide_{s}.jpg" alt="slide {s}">\n'
                if len(s_num) > 1 and n < len(s_num)-1:
                    img += '<br>'
                ha_trans.append(img)
        # add text
        ha_trans.append('<p>')
        for p in chunk:
            start = p['start']
            duration = p['end'] - p['start']
            content = p['content']
            # further process content here ########################################
            if content.endswith('།') and not content.endswith(' །'):
                content += ' '

            # unsure
            content = content.replace('༺', '<span class="unsure">༺')
            content = content.replace('༻', '༻</span>')

            # hesitation
            content = content.replace('༼', '<span class="hesit">༼')
            content = content.replace('༽', '༽</span>')

            # changed syllables
            idxs = [m.start() for m in re.finditer('࿏', content)]
            if idxs:
                raw = [content[:idxs[0]]]
                raw.extend([content[i:j] for i,j in zip(idxs, idxs[1:]+[None])])
                parts = []
                for r in raw:
                    if r.startswith('࿏'):
                        parts.append(r[:2])
                        if r[2:]:
                            parts.append(r[2:])
                    else:
                        parts.append(r)

                for i in range(len(parts)):
                    if i > 0 and parts[i].startswith('࿏'):
                        while True:
                            if not parts[i-1]:
                                break
                            c = parts[i-1][-1]
                            if c == '་':
                                break
                            parts[i] = c + parts[i]
                            parts[i-1] = parts[i-1][:-1]

                for i in range(len(parts)):
                    if '࿏' in parts[i]:
                        parts[i] = f'<span class="changed">{parts[i]}</span>'
                content = ''.join(parts)
            # #######################################################################

            # add units while ignoring empty segments
            if content.strip():
                trans = f'<a data-m="{start}" data-d="{duration}">{content}</a>'
                ha_trans.append(trans)

        ha_trans.append('</p>')

    return ''.join(ha_trans), chunks

def format_text(chunks):
    out = []
    for _, chunk in chunks:
        c = ''.join([c['content'] for c in chunk])
        out.append(c)
    return '\n\n'.join(out)

file_paths = [
    Path('components/Lamrim Dutsi Nyingpo_A_1.srt'),
    Path('components/Lamrim Dutsi Nyingpo_A_2.srt'),
    Path('components/Lamrim Dutsi Nyingpo_A_3.srt'),
    Path('components/135 A-Menag Dzö_1.srt'),
    Path('components/135 B-Menag Dzö-2.srt'),
    Path('components/137 A-Menag Dzö-3.srt'),
    Path('components/137 B-Menag Dzö-4.srt'),
    Path('components/138 A-Menag Dzö-5.srt'),
    Path('components/138 B-Menag Dzö-6.srt'),
    Path('components/139 A-Menag Dzo-7.srt'),
    Path('components/139 B-Menag Dzo-8.srt'),
    Path('components/140 A-Menag Dzö_9.srt'),
    Path('components/140 B-Menag Dzo_10.srt'),
    Path('components/141 A-Menag Dzo-11.srt'),
    Path('components/141 B-Menag Dzo-12.srt'),
    Path('components/142 A-Menag Dzo-13.srt'),
    Path('components/142 B-Menag Dzo-14.srt'),
    Path('components/143 A-Menag Dzo-15.srt'),
    Path('components/143 B-Menag Dzo-16.srt'),
    Path('components/144 A-Menag Dzo-17.srt'),
    Path('components/144 B-Menag Dzo-18.srt'),
    Path('components/112 A-Dzogchen Lamrin Yeshey Drupa.srt'),
    Path('components/112 B-Dzogchen Lamrin Yeshey Drupa.srt'),
    Path('components/113 A-Dzogchen Lamrin Yeshey Drupa.srt'),
    Path('components/155 A-Tsiksum Nedek.srt'),
    Path('components/155 B-Tsiksum Nedek.srt'),
    Path('components/001-A gol-shor-tsar-Chos.srt'),
    Path('components/Terdzod Kalop.srt'),
    Path('components/Shamatha_and_Vipashyana.srt')
]

transcriptions = []
for i, in_file in enumerate(file_paths):
    transcription, chunks = gen_ha_page(in_file)
    p = players[i] + '\n'
    p += transcript_start.replace('###', str(i+1))
    transcriptions.append(f'{p}\n{transcription}\n{transcript_end}\n\n')
    text = format_text(chunks)
    (in_file.parent.parent / (in_file.stem + '.txt')).write_text(text)

html_page = '\n'.join([head, body_beginning, '\n'.join(transcriptions), body_end])
Path('index.html').write_text(html_page)


