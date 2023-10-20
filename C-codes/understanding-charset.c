#include <stdio.h>

int main(void){
/*
 * Variable = Allocated memory in space to store value
 * We refer to a variables name to access th stored value
 * The variable now behaves as if it were the value that is stored
 * But we need to determine the type of data we want to store
 */

	int x; //Declaration
	x =  123; // Initialization
	int age = 21; // Integer(%d(decimal) as format specifier)
	float gpa = 3.9; // Floating point number(%f(float) as format specifier)
	char grade = 'A'; // Single character(%c(character) as format specifier)
	char name[] = "Nkefor Rodrick"; // Array of characters(%s(string) as format specifier)
	double exe = 9.439; //Double the precision of a float(%lf(long float) as format specifier)

	printf("Hello %s", name);
	printf("You are %d years old", age);
	
	return 0;
		}
