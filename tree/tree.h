/* All trees are binary trees unless otherwise specified */

#ifndef PRACTICE_TREE_TREE_H
#define PRACTICE_TREE_TREE_H

#ifndef max
#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif

struct tree_node {
    int data;
    struct tree_node *left;
    struct tree_node *right;
};

struct tree_node *new_node(int data);
void delete(struct tree_node *root);

#endif

