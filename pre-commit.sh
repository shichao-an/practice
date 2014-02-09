#!/bin/bash

# Astyle
astyle -r *.c *.h

# Make clean
find . -mindepth 1 -path ./.git -prune -o -type d -exec make -C {} clean \;

# Remove executales
find . -path ./.git -prune -o -path . -prune -o -type f -print -perm +111 -exec rm {} \;
