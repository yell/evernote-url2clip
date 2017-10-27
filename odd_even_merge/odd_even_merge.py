#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
from shutil import copy


def odd_even_merge(odd_dirpath='odd/', even_dirpath='even/', destination='merged/', prefix='', start_index=1):
    """Merge files from directories `odd_dirpath` and `even_dirpath` in odd-even manner
    and copy them to `destination` as '`prefix` (`start_index`)...', '`prefix` (`start_index` + 1)...', ...
    """
    if not os.path.isdir(destination):
        os.makedirs(destination)
    for dirpath, index in (
        (odd_dirpath, start_index),
        (even_dirpath, start_index + 1)
    ):
        for _, _, fnames in os.walk(dirpath):
            for fname in fnames:
                ext = fname.split('.')[-1] if '.' in fname else ''
                new_fname = "({0})".format(index)
                # new_fname = "(0.{0:01d})".format(index)
                # new_fname = "(0.{0:02d})".format(index)
                if prefix: 
                    new_fname = prefix + ' ' + new_fname
                new_fname = os.path.join(destination, new_fname)
                if ext: 
                    new_fname += ('.' + ext)
                copy(os.path.join(dirpath, fname), new_fname)
                index += 2


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--odd', type=str, default='odd/', metavar='DIRPATH',
                        help='directory with odd pages (merged collection will start from file from this directory)')
    parser.add_argument('-e', '--even', type=str, default='even/', metavar='DIRPATH',
                        help='directory with even pages')
    parser.add_argument('-d', '--destination', type=str, default='merged/', metavar='DIRPATH',
                        help='destination directory')
    parser.add_argument('-p', '--prefix', type=str, default='', metavar='PREFIX',
                        help="new filenames prefix")
    parser.add_argument('-i', '--start-index', type=int, default=1, metavar='I',
                        help='new filenames counter starts from this')
    args = parser.parse_args()
    odd_even_merge(odd_dirpath=args.odd, 
                   even_dirpath=args.even, 
                   destination=args.destination,
                   prefix=args.prefix,
                   start_index=args.start_index)


if __name__ == '__main__':
    main()
