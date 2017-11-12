#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json


def main(filepath):
    assert filepath.endswith('.ipynb')

    with open(filepath) as f:
        d = json.load(f)

    count = 0
    for cell in d['cells']:
        if cell.get('cell_type', None) != 'code':
            continue
        count += 1
        if 'execution_count' in cell:
            cell['execution_count'] = count
        if 'outputs' in cell:
            out = cell['outputs']
            if isinstance(out, list) and len(out) == 1:
                out = out[0]
            if 'execution_count' in out:
                out['execution_count'] = count

    with open(filepath, 'w') as f:
        json.dump(d, f, sort_keys=True, indent=1)


if __name__ == '__main__':
    main(sys.argv[1])
