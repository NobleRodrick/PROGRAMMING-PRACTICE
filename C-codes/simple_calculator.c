#include <stdio.h>

int main(void)
{
	char operator;
	double num1;
	double num2;
	double result;

	printf("Enter an operator(*, -, /, +): ");
	scanf("%c", &operator);

	printf("Enter a first number: ");
	scanf("%lf", &num1);

	printf("Enter a second number: ");
	scanf("%lf", &num2);
						    
	switch (operator)
	{
		case '*':
			result = num1*num2;
			printf("The product of %.2lf and %.2lf is %.2lf", num1, num2, result);
			break;
		case '-':
			result = num1-num2;
			printf("The difference of %.2lf and %.2lf is %.2lf", num1, num2, result);
			break;
		case '+':
			result = num1+num2;
			printf("The sum of %.2lf and %.2lf is %.2lf", num1, num2, result);
			break;
		case '/':
			result = num1/num2;
			printf("The ratio of %.2lf and %.2lf is %.2lf", num1, num2, result);
			break;
		default:
			printf("Please enter a valid operator");
			break;
	}
	return 0;
}
