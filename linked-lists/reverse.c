#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void printList(struct node * n) {
    while (n != NULL) {
        printf("%d ", n->data);
        n = n->next;
    }
}

void reverseList(struct node ** head) {
    struct node * prev = NULL;
    struct node * next = NULL;
    struct node * current = *head;

    while (current != NULL) {
        // First, we save the next node that we will use
        // for iterating the list at the end of the loop.
        next = current->next; 
        
        // The previous node will be the `next` one since we are reversing 
        // the linking. In the first iteration `prev` will be `NULL` 
        // but in the next ones it will have the value of the previous node.
        current->next = prev;

        // The 'current' node will be the previous handled in 
        // the next iteration. Which will be assigned to 
        // `current->next` as seen above.
        prev = current;

        // We move to the next node previously
        // saved at the beginning of the loop.
        current = next;
    }
    *head = prev;
}

struct node * reverseByNewList(struct node * oldList) {
    struct node * newList = NULL;
    struct node * element = NULL;

    while (oldList != NULL) {
        element = oldList;
        oldList = oldList->next;
        element->next = newList;
        newList = element;
    }

    return newList;
}

int main() {
    struct node * head   = NULL;
    struct node * second = NULL;
    struct node * third  = NULL;

    head   = (struct node *) malloc(sizeof(struct node));
    second = (struct node *) malloc(sizeof(struct node));
    third  = (struct node *) malloc(sizeof(struct node));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    printf("Normal list order:\n");
    printList(head);
    printf("\nReversed order:\n");
    reverseList(&head);
    printList(head);

    return 0;
}
