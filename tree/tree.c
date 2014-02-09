#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "tree.h"


struct tree_node *new_node(int data)
{
    struct tree_node *node = (struct tree_node *)malloc(sizeof(struct tree_node));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void delete(struct tree_node *root)
{
    if (root != NULL) {
        delete(root->left);
        delete(root->right);
        free(root);
    }
}

