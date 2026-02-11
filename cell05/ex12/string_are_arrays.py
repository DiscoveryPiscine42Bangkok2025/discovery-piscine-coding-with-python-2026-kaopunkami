#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    count_z = s.count("z")
    if count_z == 0:
        print("none")
    else:
        print("z" * count_z)