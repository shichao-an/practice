#include <stdio.h>
#include "sorting.h"
#define MERGE_SORT_SIZE 10

static int temp[MERGE_SORT_SIZE];


int main()
{
    int a[10] = {7, 9, 5, 1, 2, 10, 3, 4, 8, 6};
    print_integer_array(a, 10);
    merge_sort(a, temp, 0, 9);
    print_integer_array(a, 10);
    return 0;
}
