#include <stdio.h>
#include "tree.h"
#include "diameter.h"


int main()
{
    TreeNode *a, *b;
    /* Build the tree */
    TreeNode *root = new_node(1);
    b = root->left = new_node(2);
    root->right = new_node(3);
    root->right->left = new_node(4);
    a = root->right->right = new_node(5);

    /* diameter */
    int height = 0;
    printf("Diameter of root: %d\n", get_diameter(root, &height));

    /* Tree functions */
    int path[100];
    print_tree_paths(root, path, 0);
    printf("Tree sum: %d\n", get_tree_sum(root));
    printf("LCA: %d\n", get_least_common_ancestor(root, a, b)->data);
    delete(root);
    return 0;
}

