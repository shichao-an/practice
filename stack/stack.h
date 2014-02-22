#ifndef PRACTICE_STACK_STACK_H
#define PRACTICE_STACK_STACK_H

#include "list.h"

typedef List Stack;

#define stack_init list_init
#define stack_destroy list_destroy
#define stack_empty(stack) ((stack)->size == 0 ? 1 : 0)

Stack *stack_create();
void stack_push(Stack *stack, const void *data);
void *stack_pop(Stack *stack);
void *stack_top(Stack *stack);

#endif
