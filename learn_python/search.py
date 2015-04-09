import os
import sys

def search(s,p='.'):
    for i in os.listdir(p):
        if os.path.isdir(i):
            search(s, os.path.join(p,i))
        elif s in i:
            print os.path.join(os.path.abspath(p), i)

search(sys.argv[1])