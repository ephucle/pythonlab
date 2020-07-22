#!/usr/bin/env python3

from hashbang import command

@command
def echo(message):
  print(message)

if __name__ == '__main__':
  echo.execute()
