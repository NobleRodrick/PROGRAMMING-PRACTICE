void Insert(int data, int n){
    Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = NULL;
    if (n == 1){
        temp1->next = head;
        head = temp1;
        return;
    }
    Node* temp2 = head;
    for(int i = 0; i < n-2 ; i++){
        temp2 = temp2->next;
    }
    temp1->next = temp2->next;
    temp2->next = temp1;
}

int main(){
    head = NULL; //empty list
    insert(2, 1); //list: 2
    insert(3, 2); //list: 2, 3
    insert(4, 1); //list: 4, 2, 3
    insert(5, 2); //list: 4, 5, 2, 3
    //invoke th print function here
}