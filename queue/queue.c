#include <assert.h>
#include <stdlib.h>
#include "list.h"
#include "queue.h"

Queue *queue_create()
{
    Queue *queue = (Queue *)malloc(sizeof(Queue));
    queue_init(queue);
    assert(queue);
    return queue;
}

void queue_enqueue(Queue *queue, const void *data)
{
    list_insert(queue, queue->tail, data);
}


void *queue_dequeue(Queue *queue)
{
    void *data;
    list_remove_next(queue, NULL, &data);
    return data;
}


void *queue_front(Queue *queue)
{
    assert(queue->head != NULL);
    return queue->head->data;
}

