#include <assert.h>
#include <stdio.h>
#include "stack.h"


int main()
{
    Stack *stack = stack_create();
    stack_push(stack, 1);
    stack_push(stack, 2);
    int a = stack_pop(stack);
    int b = stack_pop(stack);
    assert(a == 2);
    assert(b == 1);
    assert(stack->size == 0);
    stack_destroy(stack);
    return 0;
}

