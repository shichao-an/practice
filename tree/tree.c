#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "tree.h"
#include "queue.h"


TreeNode *new_node(int data)
{
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}


/* Alternative TreeNode, which includes an extra pointer, `next` */
TreeNodeAlt *new_node_alt(int data)
{
    TreeNodeAlt *node = (TreeNodeAlt *)malloc(sizeof(TreeNodeAlt));
    assert(node != NULL);
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    node->next = NULL;
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


void delete_alt(TreeNodeAlt *root)
{
    if (root != NULL) {
        delete_alt(root->left);
        delete_alt(root->right);
        free(root);
    }
}


int get_tree_height(TreeNode *root)
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


int get_tree_sum(TreeNode *root)
{
    if (root == NULL)
        return 0;
    else {
        return (root->data + get_tree_sum(root->left)
                + get_tree_sum(root->right));
    }
}


TreeNode *get_least_common_ancestor(TreeNode *root, TreeNode *a, TreeNode *b)
{
    TreeNode *left, *right;
    if (root == NULL)
        return NULL;
    if (a == root || b == root)
        return root;
    left = get_least_common_ancestor(root->left, a, b);
    right = get_least_common_ancestor(root->right, a, b);
    /* a and b are in different sub-tree */
    if (left != NULL && right != NULL)
        return root;
    else {
        if (left != NULL)
            return left;
        else
            return right;
    }
}


void print_tree_paths(TreeNode *root, int path[], int size)
{
    if (root == NULL) {
        return;
    }

    path[size] = root->data;
    size++;

    if (root->left == NULL && root->right == NULL) {
        print_integer_array(path, size);
    } else {
        print_tree_paths(root->left, path, size);
        print_tree_paths(root->right, path, size);
    }
}


void print_integer_array(int integers[], int size)
{
    int i;
    for (i = 0; i < size; i++) {
        printf("%d ", integers[i]);
    }
    printf("\n");
}


void populate_next_right_pointers(TreeNodeAlt *root)
{
    if (root == NULL)
        return;
    if (root->left)
        root->left->next = root->right;
    if (root->right)
        root->right->next = ((root->next != NULL) ?
                             root->next->left : NULL);
    populate_next_right_pointers(root->left);
    populate_next_right_pointers(root->right);
}


TreeNode *bst_find_recursive(TreeNode *root, int data)
{
    if (root == NULL)
        return NULL;
    if (data == root->data)
        return root;
    else if (data < root->data)
        return bst_find_recursive(root->left, data);
    else
        return bst_find_recursive(root->right, data);
}


void level_order_traverse(TreeNode *root)
{
    if (root == NULL)
        return;
    Queue *queue = queue_create();
    queue_enqueue(queue, root);
    while (!queue_empty(queue)) {
        TreeNode *current = (TreeNode *)queue_dequeue(queue);
        int data = current->data;
        printf("%d\n", data);
        if (current->left != NULL)
            queue_enqueue(queue, current->left);
        if (current->right != NULL)
            queue_enqueue(queue, current->right);
    }
    queue_destroy(queue);
}

