#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <assert.h>

struct StackItem {
    int data;
    struct StackItem * next;
};

void push(struct StackItem ** stack, int data) {
    struct StackItem * new =
        (struct StackItem *) malloc(sizeof(struct StackItem));
    new->data = data;
    new->next = *stack;
    *stack = new;
}

int peek(struct StackItem * stack) {
    return stack->data;
}

int pop(struct StackItem ** stack) {
    if (stack == NULL)
        return INT_MIN;

    struct StackItem * temp = *stack;
    int item = temp->data;
    *stack = (*stack)->next;
    free(temp);

    return item;
}

int main() {
    struct StackItem * stack = NULL;

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);

    assert(3 == peek(stack));

    pop(&stack);
    assert(2 == peek(stack));
}
