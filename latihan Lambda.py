import math

def a(x):
    lambda x: x**2

def b(x,y):
    lambda x,y: math.sqrt(x**2 + y**2)

def c(*args):
    lambda *args: sum(args)/len(args)

def d(s):
    lambda s: " ".join(set(s))
