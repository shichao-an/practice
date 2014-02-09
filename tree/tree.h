/* All trees are binary trees unless otherwise specified */

#ifndef PRACTICE_TREE_TREE_H
#define PRACTICE_TREE_TREE_H

#ifndef max
#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *new_node(int data);
void delete(struct TreeNode *root);

#endif

