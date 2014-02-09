#!/bin/bash

# Make clean
find . -mindepth 1 -path "./.git" -prune -o -type d -exec make -C {} clean \;

# Remove executales
find . -path "./.git" -prune -o -type f -perm +111 -exec rm {} \;

