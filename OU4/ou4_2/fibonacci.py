# fibonacci.py

import ctypes
lib = ctypes.cdll.LoadLibrary('./libfibonacci.so')

def fib(n):
	return lib.fib_c(n)
