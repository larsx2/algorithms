#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node * next;
};

void printList(struct node * n) {
    while (n != NULL) {
        printf("%d ", n->data);
        n = n->next;
    }
}

// Insert a node at the beginning of the list, making it the new head
void preppend(struct node ** head, int new_data) {
    struct node * new_node = (struct node*) malloc(sizeof(struct node));
    new_node->data = new_data;
    new_node->next = *head;
    *head = new_node;
}

// Append a node to the end of the list
void append(struct node ** head, int new_data) {
    struct node* new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = new_data;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return;
    }

    struct node* current = (*head);
    while (current->next != NULL)
        current = current->next;

    current->next = new_node;
}

int main() {
    struct node * head = NULL;
    append(&head, 1);
    append(&head, 2);
    append(&head, 3);
    preppend(&head, 2);
    preppend(&head, 3);
    printList(head);
}
