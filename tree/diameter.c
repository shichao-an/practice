#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "tree.h"
#include "diameter.h"


int get_diameter(TreeNode *root, int *height)
{
    int left_h = 0, right_h = 0;
    int left_d = 0, right_d = 0;

    if (root == NULL) {
        *height = 0;
        return 0;
    }

    left_d = get_diameter(root->left, &left_h);
    right_d = get_diameter(root->right, &right_h);

    *height = max(left_h, right_h) + 1;

    return max(max(left_d, right_d), left_h + right_h + 1);
}

int main()
{
    TreeNode *root = new_node(1);
    root->left = new_node(2);
    root->right = new_node(3);
    root->right->left = new_node(4);
    int height = 0;
    printf("Diameter of root: %d\n", get_diameter(root, &height));
    delete(root);
    return 0;
}

