#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "tree.h"


TreeNode *new_node(int data)
{
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void delete(TreeNode *root)
{
    if (root != NULL) {
        delete(root->left);
        delete(root->right);
        free(root);
    }
}

