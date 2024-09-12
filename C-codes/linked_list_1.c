#include <stdlib.h>
#include <stdio.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* head; //global variable, can be accessed anywhere
void Insert();
void Print();
int main(){
    head = NULL; //empty list
    printf("How many numbers? \n");
    int n, i, x;
    scanf("%d", &n);
    for ( i = 0; i < n; i++)
    {
        printf("Enter the number \n");
        scanf("%d", &x);
        Insert(x);
        Print();
    }
}


void Insert(int x){
    struct Node* temp = (Node*)malloc(sizeof(struct Node));
    temp -> data = x;
    temp -> next = head;
    head = temp;
}

void Print(){
    struct Node* temp = head;
    printf("List is: ");
    while(temp != NULL){
        printf("%d", temp->data);
        temp=temp->next;
    }
    printf("\n");
}
