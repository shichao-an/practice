#ifndef PRACTICE_QUEUE_QUEUE_H
#define PRACTICE_QUEUE_QUEUE_H

#include "list.h"

typedef List Queue;

#define queue_init list_init
#define queue_destroy list_destroy
#define queue_empty(queue) ((queue)->size == 0 ? 1 : 0)

Queue *queue_create();
void queue_enqueue(Queue *queue, const int data);
int queue_dequeue(Queue *queue);
int queue_front(Queue *queue);


#endif
