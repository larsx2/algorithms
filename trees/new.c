#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node * new(int data) {
    struct node * node = (struct node *) malloc(sizeof(struct node));

    node->data = data;

    node->left = NULL;
    node->right = NULL;

    return node;
}

int main() {
    struct node * root = new(1);
    root->left = new(2);
    root->right = new(3);

    root->left->left = new(4);

    getchar();

    return 0;
}
