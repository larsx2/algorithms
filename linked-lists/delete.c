#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node * next;
};

void printList(struct node * node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

void push(struct node ** head, int new_data) {
    struct node * new_node = (struct node *) malloc(sizeof(struct node));

    new_node->data = new_data;
    new_node->next = *head;
    *head = new_node;
}

void delete(struct node ** head, int data) {
    struct node * prev = NULL;
    struct node * current = *head;

    // handle case where head is the node we are looking for
    if (current != NULL && current->data == data) {
        *head = current->next;
        free(current);
        return;
    }

    while (current != NULL && current->data != data) {
        prev = current;
        current = current->next;
    }

    if (current == NULL)
        return;

    prev->next = current->next;

    free(current);
}

int main() {
    struct node * head = NULL;

    push(&head, 3);
    push(&head, 2);
    push(&head, 1);

    puts("Created linked list: ");
    printList(head);
    delete(&head, 1);
    printList(head);

    return 0;
}
