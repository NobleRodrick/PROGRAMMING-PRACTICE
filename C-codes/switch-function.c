#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char grade;

	printf("Please enter a grade: ");
	scanf("%c", &grade);

	switch(grade)
	{
		case 'A':
			printf("Excellent!!!\n");
			break;
		case 'B':
			printf("Very good!!\n");
			break;
		case 'C':
			printf("Not Bad!\n");
			break;
		case 'D':
			printf("Not too bad!\n");
			break;
		case 'F':
			printf("Wow, you just failed\n");
			break;
		default:
			printf("please enter a valid grade\n");
			break;
	}
	return 0;
}
