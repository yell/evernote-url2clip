# odd-even-merge

Usage:
```bash
$ python odd_even_merge.py -h
usage: odd_even_merge.py [-h] [-o DIRPATH] [-e DIRPATH] [-d DIRPATH]
                         [-p PREFIX] [-i I] [-t STR]

optional arguments:
  -h, --help            show this help message and exit
  -o DIRPATH, --odd DIRPATH
                        directory with odd files, merged collection will start
                        from file from this directory (default: odd/)
  -e DIRPATH, --even DIRPATH
                        directory with even files, leave empty if you just
                        want to rename files (default: even/)
  -d DIRPATH, --destination DIRPATH
                        destination directory (default: merged/)
  -p PREFIX, --prefix PREFIX
                        new filenames prefix (default: )
  -i I, --start-index I
                        new filenames counter starts from this (default: 1)
  -t STR, --index-template STR
                        python template for index, e.g. for '(0.0x)' use
                        (0.{0:02d}) (default: ({0}))
```
