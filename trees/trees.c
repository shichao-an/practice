#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "trees.h"


struct node *new_node(int data)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void delete(struct node *root)
{
    if (root != NULL) {
        delete(root->left);
        delete(root->right);
        free(root);
    }
}

