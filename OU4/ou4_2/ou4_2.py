#!/usr/bin/env python3

from heltal import Heltal
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1)+fib_py(n-2)

def main():
	rng = list(range(30,45))

	py_times = []
	cpp_times = []

	for n in rng:
		tic = pc()
		fib_py(n)
		toc = pc()
		py_times.append(round(toc-tic,2))

	f = Heltal(0)
	for n in rng:
		f.set(n)
		tic = pc()
		f.fib()
		toc = pc()
		cpp_times.append(round(toc-tic,2))

	print(f"Python times: {py_times}")
	print(f"C++ times: {cpp_times}")

	fig, ax = plt.subplots()
	ax.plot(rng,py_times,'r--',label='Python')
	ax.plot(rng,cpp_times,'k-',label='C++')
	ax.set_title('Time comparison for Fibonacci calculations')
	ax.set_xlabel('n')
	ax.set_ylabel('Seconds')
	legend=ax.legend(loc='upper left', shadow=True,fontsize='small')
	plt.savefig('fib_times.pdf')

if __name__ == '__main__':
	main()
