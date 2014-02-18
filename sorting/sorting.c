#include <stdlib.h>
#include <stdio.h>
#include "sorting.h"


void merge(int a[], int t[], int left, int mid, int right)
{
    int i;
    int p = left;
    int left_end = mid - 1;
    int size = right - left + 1;

    /* Compare each element from the two parts and copy to `t` */
    while ((left <= left_end) && (mid <= right)) {
        if (a[left] <= a[mid])
            t[p++] = a[left++];
        else
            t[p++] = a[mid++];
    }

    /* Copy the rest elements of either part to `t` */
    while (left <= left_end) {
        t[p++] = a[left++];
    }

    while (mid <= right) {
        t[p++] = a[mid++];
    }

    /* Copy each elements in `t` back to `a` */
    for (i = 0; i < size; i++) {
        a[right] = t[right];
        right--;
    }
}


void merge_sort(int a[], int t[], int left, int right)
{
    int mid;
    if (left < right) {
        mid = (left + right) / 2;
        merge_sort(a, t, left, mid);
        merge_sort(a, t, mid + 1, right);
        merge(a, t, left, mid + 1, right);
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

