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

int length(struct node * head) {
    struct node * current = head;
    int count = 0;

    while (current != NULL) {
        current = current->next;
        count++;
    }

    return count;
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

    printf("We have a list of %d nodes: ", length(head));
    printList(head);

    return 0;
}
