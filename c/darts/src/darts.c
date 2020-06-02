#include "darts.h"
#include <math.h>

int score(coordinate_t landing_position) {
	float radius = sqrt(pow(landing_position.x, 2) + pow(landing_position.y, 2));

	if (radius > 10) {
		return 0;
	}
	else if (radius <= 10 && radius > 5) {
		return 1;
	}
	else if (radius <= 5 && radius > 1) {
		return 5;
	}
	else {
		return 10;
	}
}
