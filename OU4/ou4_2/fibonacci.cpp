// fibonacci.cpp

int fib(int n){
	if (n <= 1){
		return n;
	} else {
		return fib(n-1)+fib(n-2);
	}
};

extern "C"{
	int fib_c(int n) {return fib(n);}
}
