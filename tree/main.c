#include <stdio.h>
#include "tree.h"
#include "diameter.h"


static TreeNode *create_tree()
{
    TreeNode *root = new_node(1);
    root->left = new_node(2);
    root->right = new_node(3);
    root->right->left = new_node(4);
    root->right->right = new_node(5);
    return root;
}


static TreeNodeAlt *create_tree_alt()
{
    TreeNodeAlt *root = new_node_alt(1);
    root->left = new_node_alt(2);
    root->right = new_node_alt(3);
    root->right->left = new_node_alt(4);
    root->right->right = new_node_alt(5);
    return root;
}


int main()
{
    TreeNode *root, *a, *b;
    TreeNodeAlt *root_alt;

    /* Build the trees */
    root = create_tree();
    root_alt = create_tree_alt();
    b = root->left;
    a = root->right->right;

    /* diameter */
    int height = 0;
    printf("Diameter of root: %d\n", get_diameter(root, &height));

    /* Tree functions */
    int path[100];
    print_tree_paths(root, path, 0);
    printf("Tree sum: %d\n", get_tree_sum(root));
    printf("LCA: %d\n", get_least_common_ancestor(root, a, b)->data);

    populate_next_right_pointers(root_alt);

    delete(root);
    delete_alt(root_alt);
    return 0;
}

