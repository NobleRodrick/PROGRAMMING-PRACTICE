//linked list: Delete a node at nth position
#include<stdio.h>
#include<stdlib.h>
 
struct Node{
    int data;
    struct Node* next;
};
struct Node* head; //global
void Insert(int data); //insert an integer at and of list
void Print(); // print all elements in the list
void Delete(int n); //delete node at position n
int main(){
    head = NULL; //empty list
    insert(2); // have been implemented in previous lessons
    insert(4);
    insert(6);
    insert(5); //list : 2, 4, 6, 5
    Print();
    int n;
    printf("Enter a position\n");
    scanf("%d",&n);
    Delete(n);
    Print(); //have been implemented in previous lessons
}


//Deletes node at position n
void Delete(int n){
    struct Node* temp1 = head;
    if(n == 1){
        head = temp1->next; //head now points to second node
        free(temp1);
        return;
    }
    int i;
    for(i = 0; i <n-2; i++){
        temp1 = temp1->next;
    // temp1 points to (n-1)th Node
    struct Node* temp2 = temp1->next; //nth node
    temp1->next = temp2->next; //(n+1)th node
    free(temp2); // delete temp2
    }
}