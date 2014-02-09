#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "tree.h"


struct TreeNode *new_node(int data)
{
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void delete(struct TreeNode *root)
{
    if (root != NULL) {
        delete(root->left);
        delete(root->right);
        free(root);
    }
}

