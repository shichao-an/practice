#!/bin/bash

# Astyle
astyle -r *.c *.h

# Make clean
find . -mindepth 1 -path ./.git -prune -o -type d -exec make -C {} clean \;

# Remove executales
find . -mindepth 2 -path ./.git -prune -o  -type f -perm +111 -exec rm {} \;
