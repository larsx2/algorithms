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

void push(struct node ** head, int data) {
    struct node * new = (struct node *) malloc(sizeof(struct node));
    new->data = data;
    new->next = *head;
    (*head) = new;
}

struct node * last(struct node * head, int n) {
    struct node * current = head;
    struct node * nth = head;
    int lo = 0, hi = 0;

    while (current != NULL) {
        if ((hi - n) == lo) {
            lo++;
            nth = nth->next;
        }
        hi++;
        current = current->next;
    }

    return nth;
}

int main() {
    struct node * head   = NULL;

    push(&head, 1);
    push(&head, 2);
    push(&head, 3);
    push(&head, 4);
    push(&head, 5);
    push(&head, 6);
    printList(head);

    struct node * nth = last(head, 2);
    printf("\n%d at %p\n", nth->data, nth);

    return 0;
}
