#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "stack.h"
#include "list.h"


Stack *stack_create()
{
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    assert(stack);
    stack_init(stack);
    return stack;
}


void stack_push(Stack *stack, const void *data)
{
    list_insert(stack, NULL, data);
}


void *stack_pop(Stack *stack)
{
    void *data;
    list_remove_next(stack, NULL, &data);
    return data;
}


void *stack_top(Stack *stack)
{
    assert(stack->head != NULL);
    return stack->head->data;
}

