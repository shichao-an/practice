#include <assert.h>
#include <stdio.h>
#include "queue.h"


int main()
{
    Queue *queue = queue_create();
    int data1 = 1;
    int data2 = 2;
    queue_enqueue(queue, &data1);
    queue_enqueue(queue, &data2);
    int *t = (int *)queue_front(queue);
    assert(*t == 1);
    assert(!queue_empty(queue));
    int *a = (int *)queue_dequeue(queue);
    int *b = (int *)queue_dequeue(queue);
    assert(*a == 1);
    assert(*b == 2);
    assert(queue_empty(queue));
    queue_destroy(queue);
    return 0;
}

