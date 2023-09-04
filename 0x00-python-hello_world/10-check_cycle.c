#include "lists.h"

/**
 * checkCycle -Function that checks if the linked list has a cycle
 * @list: linked list being checked
 * Return: 1 if the list has a cycle and 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
