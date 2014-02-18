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

