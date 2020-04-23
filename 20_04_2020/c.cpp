#include <iostream>
#include <bits/stdc++.h>
#include <inttypes.h>

using namespace std;

class Node {
    public:
        int data;
        Node* both;
};

Node* XOR(Node *a, Node *b){
    return (Node *) ((uintptr_t)(a) ^ (uintptr_t)(b));
}

void add(Node **head, int data)
{
    Node *new_node = new Node();
    new_node->data = data;
    new_node->both = *head;

    if (*head != NULL)
    {
      (*head)->both = XOR((*head)->both, new_node);
    }
    *head = new_node;
}
void del(Node *head, int index)
{
    Node* temp = head;
    Node* prev = NULL;
    Node* next = NULL;
    while (temp != NULL)
    {
        next = XOR(prev, temp->both);
        if (index == temp->data)
        {
          if(temp == head)
          {
              next->both = XOR(next->both,head);
              head = next;
              delete(temp);
              return;
          }
          cout<< "DATA:" << prev->data << ":" << temp->data << ":" << next->data<< endl;
          prev->both = XOR(XOR(prev->both,temp), next);
          next->both = XOR(prev,XOR(next->both,temp));
          delete(temp);
          return;
        }
       prev = temp;
       temp = next;
    }
    cout <<"index gives does not belong in list" << endl;
}
void print(Node *head, int index)
{
    Node* temp = head;
    Node* prev = NULL;
    Node* next = NULL;
    while (temp != NULL)
    {
        if (index == 0)
        {
          cout << temp->data << endl;
          return;
        }
        next = XOR(prev, temp->both);

        prev = temp;
        temp = next;
        index --;
    }
    if (index !=0)
    {
      cout <<"index gives does not belong in list" << endl;
    }
}
void print1(Node *head)
{
    Node* temp = head;
    Node* prev = NULL;
    Node* next = NULL;
    while (temp != NULL)
    {
          cout << temp->data << endl;
        next = XOR(prev, temp->both);

        prev = temp;
        temp = next;
    }
}


int main()
{
    Node *head = NULL;
    add(&head, 1);
    add(&head, 2);
    add(&head, 3);
    add(&head, 4);
    add(&head, 5);
    add(&head, 6);
    del(head, 1);
    print(head, 5);
    print1(head);
    return 0;
}
