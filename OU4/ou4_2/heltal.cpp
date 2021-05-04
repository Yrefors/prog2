#include <cstdlib>
// Integer class 

class Heltal{
	private:
		int val;
		int pfib(int n);
	public:
		Heltal(int);
		int get();
		void set(int);
		int fib(){
			return pfib(val); 
		}
	};
 
Heltal::Heltal(int n){
	val = n;
	}
 
int Heltal::get(){
	return val;
	}
 
void Heltal::set(int n){
	val = n;
	}

int Heltal::pfib(int n){
	if (n <= 1){
		return n;
	} else {
		return pfib(n-1)+pfib(n-2);
	}
}

extern "C"{
	Heltal* Heltal_new(int n) {return new Heltal(n);}
	int Heltal_get(Heltal* heltal) {return heltal->get();}
	void Heltal_set(Heltal* heltal, int n) {heltal->set(n);}
	void Heltal_delete(Heltal* heltal){
		if (heltal){
			delete heltal;
			heltal = nullptr;
			}
		}
	int Heltal_fib(Heltal* heltal) {heltal->fib();}
	}
