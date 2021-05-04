
#!/usr/bin/env python3

from fibonacci import fib_cpp, fib_py
from time import perf_counter as pc

def main():
	rng = 40
	print(f"Range: {rng}")
	tic = pc()
	for n in range(rng):
		#print(fib_cpp(n))
		fib_cpp(n)
	toc = pc()
	time_cpp = toc-tic

	tic = pc()
	for n in range(rng):
		#print(fib_py(n))
		fib_py(n)
	toc = pc()
	time_py = toc-tic

	print(f"Calculations of fib(n) for n=0 to n={rng}")
	print(f"Time C++: {time_cpp:0.2f}")
	print(f"Time python: {time_py:0.2f}")

if __name__ == '__main__':
	main()
