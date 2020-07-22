#!/usr/bin/env python3

import os
from hashbang import command

@command
def pwd():
    return os.getcwd()

if __name__ == '__main__':
    pwd.execute()
