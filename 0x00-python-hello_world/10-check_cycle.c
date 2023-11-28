#include "lists.h"

/**
  *check_cycle - checks whether the linked list has a circle
  *@list: first node of the list
  *Return: Integer (0 for no circle, 1 for circle found)
  */

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	while(hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if(hare == tortoise)
			return (1);
	}
	return (0);
}
