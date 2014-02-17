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


int get_tree_height(struct TreeNode *root)
{
    int left_h, right_h;
    if (root == NULL)
        return -1;
    else {
        left_h = get_tree_height(root->left);
        right_h = get_tree_height(root->right);
        return max(left_h, right_h) + 1;
    }
}
