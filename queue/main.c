#include <assert.h>
#include <stdio.h>
#include "queue.h"


int main()
{
    Queue *queue = queue_create();
    queue_enqueue(queue, 1);
    queue_enqueue(queue, 2);
    int t = queue_front(queue);
    assert(t == 1);
    assert(!queue_empty(queue));
    int a = queue_dequeue(queue);
    int b = queue_dequeue(queue);
    assert(a == 1);
    assert(b == 2);
    assert(queue_empty(queue));
    queue_destroy(queue);
    return 0;
}

