#ifndef PRACTICE_LIST_LIST_H
#define PRACTICE_LIST_LIST_H

typedef struct ListNode {
    int data;
    struct ListNode *next;
} ListNode;

typedef struct List {
    int size;
    ListNode *head;
    ListNode *tail;
} List;

#endif
