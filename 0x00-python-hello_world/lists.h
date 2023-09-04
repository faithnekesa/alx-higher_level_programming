#ifndef LISTS_HEADER
#define LISTS_HEADER

#include <stdlib.h>

/**
 * struct listint_s -Struct for singly linked list
 * @n: integer
 * @next:Node ointing to the next node
 * Description:Struct for singly linked list node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif

