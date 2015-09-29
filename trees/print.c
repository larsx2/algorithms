#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node * left;
    struct node * right;
};

struct node * new(int data) {
    struct node * node = (struct node *) malloc(sizeof(struct node));

    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return node;
}

void printPostorder(struct node * node) {
    if (node == NULL)
        return;

    printPostorder(node->left);
    printPostorder(node->right);

    printf("%d ", node->data);
}

void printInorder(struct node * node) {
    if (node == NULL)
        return;

    printInorder(node->left);
    printf("%d ", node->data);
    printInorder(node->right);
}

void printPreorder(struct node * node) {
    if (node == NULL)
        return;

    printf("%d ", node->data);

    printPreorder(node->left);
    printPreorder(node->right);
}

int main() {
    struct node * root = new(1);
    root->left = new(2);
    root->right = new(3);

    root->left->left = new(4);
    root->left->right = new(5);

    printf("\nPreorder traversal of binary tree is \n");
    printPreorder(root);

    printf("\nInorder traversal of binary tree is \n");
    printInorder(root);

    printf("\nPostorder traversal of binary tree is \n");
    printPostorder(root);
}
