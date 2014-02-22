#include <assert.h>
#include <stdio.h>
#include "stack.h"


int main()
{
    Stack *stack = stack_create();
    int data1 = 1;
    int data2 = 2;
    stack_push(stack, &data1);
    stack_push(stack, &data2);
    int *t = (int *)stack_top(stack);
    assert(*t == 2);
    assert(!stack_empty(stack));
    int *a = (int *)stack_pop(stack);
    int *b = (int *)stack_pop(stack);
    assert(*a == 2);
    assert(*b == 1);
    assert(stack_empty(stack));
    stack_destroy(stack);
    return 0;
}

