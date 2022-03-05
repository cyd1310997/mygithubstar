
######################################
import os
import shutil
import argparse
import sys
import threading
import time
import sqlite3
import re
import uuid
######################################


def main():
    with open('nav.githubstar.md', 'r') as f:
        L = f.readlines()
    L = [i.strip() for i in L]
    L = sorted(set(L),key=L.index)
    L = sorted(L)
    with open('nav.githubstar.sorted.md', 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('ok')

if __name__ == '__main__':
    main()
    