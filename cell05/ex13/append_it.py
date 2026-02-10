import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for p in params:
        if p.endswith("ism"):
            continue
        print(p + "ism")