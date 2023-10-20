#include <stdio.h>

void sort(int array[], int size)        //Bubble sort
{
	for(int i = 0; i < size - 1; i++)
	{
		for(int j = 0; j < size - i - 1; j++)
		{
			if(array[j] > array[j + 1])
			{
				int temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
}
					
void printArray(int array[], int size)
{
	for(int i = 0;i < size; i++)
	printf("%d\n", array[i]);
}

int main()
{
	int array[] = {9, 1, 8, 2, 3, 4, 5, 7, 6};
	int size = sizeof(array)/sizeof(array[0]);

	sort(array, size);
	printArray(array, size);
}
