#!/usr/bin/env bash
git diff -p -R --no-color \
    | grep -E "^(diff|(old|new) mode)" --color=never  \
    | git apply
