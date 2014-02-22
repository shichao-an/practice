#ifndef PRACTICE_QUEUE_QUEUE_H
#define PRACTICE_QUEUE_QUEUE_H

#include "list.h"

typedef List Queue;

#define queue_init list_init
#define queue_destroy list_destroy
#define queue_empty(queue) ((queue)->size == 0 ? 1 : 0)

Queue *queue_create();
void queue_enqueue(Queue *queue, const void *data);
void *queue_dequeue(Queue *queue);
void *queue_front(Queue *queue);


#endif
