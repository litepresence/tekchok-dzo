#!/usr/bin/env python3
import os, re, sys
try:
    import pyewts
except ImportError:
    print('Error: pyewts not installed', file=sys.stderr)
    sys.exit(1)
converter = pyewts.pyewts()

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out = []
    for line in lines:
        m = re.match(r'^(\d+\.\s+)(.*)', line)
        if m:
            out.append(m.group(1) + converter.toWylie(m.group(2)))
        else:
            out.append(converter.toWylie(line.strip()))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(chr(10).join(out) + chr(10))

os.makedirs('wylie', exist_ok=True)
files = sorted([f for f in os.listdir('tibetan') if f.endswith('.txt')])
print(f'Processing {len(files)} files...')
for fn in files:
    try:
        process_file(os.path.join('tibetan', fn), os.path.join('wylie', fn))
        print(f'  OK {fn}')
    except Exception as e:
        print(f'  FAIL {fn}: {e}')
print('Done!')
