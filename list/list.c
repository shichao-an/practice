#include <stdlib.h>
#include "list.h"


void list_init(List *list)
{
    list->size = 0;
    list->head = NULL;
    list->tail = NULL;
}
