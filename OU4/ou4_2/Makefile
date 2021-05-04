# Makefile for OU4
all:
	g++ -c -fPIC fibonacci.cpp -o fibonacci.o
	g++ -shared -o libfibonacci.so  fibonacci.o	
clean:
	rm -fr *.o *.so __pycache__
