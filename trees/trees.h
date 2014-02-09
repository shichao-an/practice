/* All trees are binary trees unless otherwise specified */

#ifndef PRACTICE_TREES_H
#define PRACTICE_TREES_H

#ifndef max
#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node *new_node(int data);
void delete(struct node *root);

#endif

