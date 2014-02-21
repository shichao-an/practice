#include <assert.h>
#include <stdio.h>
#include "stack.h"


int main()
{
    Stack *stack = stack_create();
    stack_push(stack, 1);
    stack_push(stack, 2);
    int t = stack_top(stack);
    assert(t == 2);
    assert(!stack_empty(stack));
    int a = stack_pop(stack);
    int b = stack_pop(stack);
    assert(a == 2);
    assert(b == 1);
    assert(stack_empty(stack));
    stack_destroy(stack);
    return 0;
}

