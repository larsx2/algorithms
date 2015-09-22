#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define bool int

struct node {
    char data;
    struct node * next;
};

void push(struct node ** head, char data) {
    struct node * new = (struct node *) malloc(sizeof(struct node));
    new->data = data;
    new->next = *head;
    *head = new;
}

char pop(struct node ** head) {
    if (*head == NULL) {
        return '\0';
    }

    struct node * temp = *head;
    char value = temp->data;

    *head = (*head)->next;
    free(temp);
    return value;
}

bool isMatch(char a, char b) {
    if (a == '(' && b == ')') {
        return 1;
    }
    else if (a == '[' && b == ']') {
        return 1;
    }
    else if (a == '{' && b == '}') {
        return 1;
    }
    else {
        return 0;
    }
}

bool validate(char * exp) {
    struct node * stack = NULL;

    for (int i=0; i < strlen(exp); i++) {
        if (exp[i] == '(' || exp[i] == '[' || exp[i] == '{')  {
            push(&stack, exp[i]);
        }
        else if (exp[i] == ')' || exp[i] == ']' || exp[i] == '}') {
            char prev = pop(&stack);

            if (! isMatch(prev, exp[i])) {
                printf("Does not match '%c' and '%c'", prev, exp[i]);
                return 0;
            }
        }
        else {
            printf("Invalid character!");
        }
    }

    if (pop(&stack)) {
        printf("Stack not empty!");
        return 0;
    }

    return 1;
}

int main() {
    char exp[100] = "[[{}]]()";

    printf("Validating the following expression: %s", exp);
    if (validate(exp)) {
        printf("\nBalanced!");
    }
    else {
        printf("\nUnbalanced!");
    }

    return 0;
}
