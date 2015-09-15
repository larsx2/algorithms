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
    // handle list being empty
    if (*head == NULL) {
        printf("Empty list!");
        return;
    }

    // handle head being the one we look for
    if ((*head)->data == data) {
        *head = (*head)->next;
        return;
    }
    
    // iterate list
    struct node * current = (struct node *) malloc(sizeof(struct node));
    while (current->next != NULL) {
        if (current->next->data == data) {
            current->next = current->next->next;
            break;
        }
        current = current->next;
    }

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
