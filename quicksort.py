#!/usr/bin/env python3

from itertools import tee
from itertools import chain
import random
import time
import types

h = [random.randrange(0,1000000) for i in range(100000, 0, -1)]

h1 = iter(h) 
h2 = iter(h) 

def Tsort(i):
  stack = wrap(i)
  head = next(stack, False)
  while head:
    if isinstance(head, int):
      yield head
    else:
      try:
        pivot = next(head)
        smaller, larger = split(pivot, head)
        stack = chain(wrap(smaller), [pivot], wrap(larger), stack)
      except StopIteration:
        head = next(stack, False)
        continue
    head = next(stack, False)

def wrap(i):
  yield i

def split(p, i):
  s, l = tee(i)
  def smaller():
    for e in s:
      if e < p:
        yield e
  def larger():
    for e in l:
      if not(e < p):
        yield e
  return smaller(), larger()


print("starting sorting")

print("Ted's sorting")
start = time.time()
y = Tsort(h2)
print(next(y))
print(time.time() - start)

print("default sorting")
start = time.time()
y = sorted(h1)
print(next(iter(y)))
print(time.time() - start)
