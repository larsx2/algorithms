#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct Stack {
    int top;
    unsigned capacity;
    int * array;
};

struct Stack * create(unsigned capacity) {
    struct Stack * stack = (struct Stack *) malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int *) malloc(stack->capacity * sizeof(int));

    return stack;
}

int isFull(struct Stack * stack) {
    return stack->top == stack->capacity - 1;
}

void push(struct Stack * stack, int item) {
    if (! isFull(stack)) {
        stack->array[++stack->top] = item;
        printf("%d pushed to stack\n", item);
    }
}

int main() {
    struct Stack * stack = create(100);

    push(stack, 10);
    push(stack, 20);
    push(stack, 30);

    return 0;
}

