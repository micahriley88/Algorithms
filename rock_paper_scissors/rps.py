#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = ['Rock', 'Paper', 'Scissors']
  outcomes=[]
  def helper(n):
    if n == 0:
      return outcomes
    if n > 1:
      



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')