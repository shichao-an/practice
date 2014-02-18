/* All trees are binary trees unless otherwise specified */

#ifndef PRACTICE_TREE_TREE_H
#define PRACTICE_TREE_TREE_H

#ifndef max
#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif

typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;


TreeNode *new_node(int data);
void delete(TreeNode *root);
int get_tree_height(TreeNode *root);
int get_tree_sum(TreeNode *root);
TreeNode *get_least_common_ancestor(TreeNode *root, TreeNode *a, TreeNode *b);
void print_tree_paths(TreeNode *root, int integers[], int size);
void print_integer_array(int integers[], int size);

#endif

