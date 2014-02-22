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

void queue_enqueue(Queue *queue, const int data)
{
    list_insert(queue, queue->tail, data);
}


int queue_dequeue(Queue *queue)
{
    int data;
    list_remove_next(queue, NULL, &data);
    return data;
}


int queue_front(Queue *queue)
{
    assert(queue->head != NULL);
    return queue->head->data;
}

