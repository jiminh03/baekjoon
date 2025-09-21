import sys

A, B, V = map(int, sys.stdin.readline().split())

D = A - B
days = (V - B + D - 1) // D

print(days)