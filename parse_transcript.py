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
        s = {'start': start, 'end': end, 'content': content}
        parsed.append(s)
    return parsed

def gen_ha_page(in_file):
    # A. parse and prepare chunks
    parsed = parse_srt(in_file)
    chunks = []
    cur = []
    slide_num = 0
    for p in parsed:
        if p['content'].startswith('{'):
            # add to chunks
            if cur:
                num = None
                if slide_num:
                    num = slide_num
                chunks.append((num, cur))
                cur = []

            # start new chunk
            s_num, text = p['content'].split('}')
            slide_num = int(s_num[1:])
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
            img = f'\n<img src="components/slides/slide_{s_num}.jpg" alt="slide {s_num}">\n'
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

    return ''.join(ha_trans)


in_file = 'components/Lamrim Dutsi Nyingpo_A_1.srt'
transcription = gen_ha_page(in_file)
html_page = '\n'.join([head, body_beginning, transcript_start, transcription, transcrip_end, body_end])

Path('index.html').write_text(html_page)
