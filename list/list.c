#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "list.h"


void list_init(List *list)
{
    list->size = 0;
    list->head = NULL;
    list->tail = NULL;
}


void list_insert(List *list, ListNode *list_node, const int data)
{
    ListNode *new_node = (ListNode *)malloc(sizeof(ListNode));
    assert(new_node);
    new_node->data = data;

    /* Insert at the head */
    if (list_node == NULL) {
        if (list->size == 0)
            list->tail = new_node;

        new_node->next = list->head;
        list->head = new_node;
    }

    /* Insert after `list_node` */
    else {
        /* Insert at the end */
        if (list_node->next == NULL) {
            list->tail = new_node;
        }
        new_node->next = list_node->next;
        list_node->next = new_node;
    }

    list->size++;
}


/* Remove the list node next to `list_node`
 * Data of the removed node will be stored in `data`
 */
void list_remove_next(List *list, ListNode *list_node, int *data)
{
    ListNode *old_node;
    assert(list->size > 0);

    /* Remove the head node */
    if (list_node == NULL) {
        old_node = list->head;
        *data = old_node->data;
        list->head = old_node->next;

        if (list->size == 1) {
            list->tail = NULL;
        }
    }

    else {
        /* `list_node` cannot be the tail node */
        assert(list_node->next != NULL);
        old_node = list_node->next;
        list_node->next = old_node->next;

        if (list_node->next == NULL)
            list->tail = list_node;
    }

    free(old_node);

    list->size--;

}


/* Destroy a list using `list_remove_next()` */
void list_destroy(List *list)
{
    int data;
    assert(list->size > 0);
    while (list->size > 0) {
        list_remove_next(list, NULL, &data);
    }
    free(list);
}


/* Alternative to `list_destroy()` */
void list_destroy_alt(List *list)
{
    assert(list->size > 0);
    ListNode *head = list->head;
    while (head) {
        ListNode *next = head->next;
        free(head);
        head = next;
    }
    free(list);
}


void print_list(List *list)
{
    ListNode *head = list->head;
    while (head) {
        printf("%d", head->data);
        if (head != list->tail) {
            printf("-->");
        }
        head = head->next;
    }
    putchar('\n');
}


int main()
{
    List *list = (List *)malloc(sizeof(List));
    assert(list);
    list_init(list);
    list_insert(list, NULL, 1);
    list_insert(list, list->tail, 2);
    list_insert(list, list->tail, 3);
    list_insert(list, NULL, 4);
    print_list(list);
    list_destroy_alt(list);
    return 0;
}

