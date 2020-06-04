#include "resistor_color.h"



resistor_band_t color_array[] = {BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE};

int color_code(resistor_band_t color) {
	return color_array[color];
}


resistor_band_t* colors(void) {
	return color_array;
}
