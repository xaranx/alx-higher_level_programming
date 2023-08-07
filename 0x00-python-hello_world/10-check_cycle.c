#include "lists.h"

/**
 *check_cycle - check if the linked list containa cycle
 *@list: list
 *Return: 1 if there is a cycle 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
