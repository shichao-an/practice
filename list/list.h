#ifndef PRACTICE_LIST_LIST_H
#define PRACTICE_LIST_LIST_H


typedef struct ListNode {
    void *data;
    struct ListNode *next;
} ListNode;


typedef struct List {
    int size;
    ListNode *head;
    ListNode *tail;
} List;


void list_init(List *list);
void list_insert(List *list, ListNode *list_node, const void *data);
void list_remove_next(List *list, ListNode *list_node, void **data);
void list_destroy(List *list);
void list_destroy_alt(List *list);
void list_print(List *list);

#endif
