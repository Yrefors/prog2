# fibonacci.py

import ctypes
lib = ctypes.cdll.LoadLibrary('./libfibonacci.so')

def fib_cpp(n):
	return lib.fib_c(n)

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1)+fib_py(n-2)
