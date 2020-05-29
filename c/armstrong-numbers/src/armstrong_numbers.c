#include "armstrong_numbers.h"
#include "math.h"


int is_armstrong_number(int candidate) {
	int length = 0;
	int original_num = candidate;
	int calc = 0;
	int rem = 0;

	while (candidate != 0){
		candidate/=10;
		++length;
	}
	candidate = original_num;

	while (candidate != 0){
		rem=candidate % 10;
		calc+=pow(rem, length);
		candidate = candidate /10;

	}

	//printf("calc :%d length: %d", calc, length);

	if (calc != original_num){
		return 0;
	}

	return 1;
}
