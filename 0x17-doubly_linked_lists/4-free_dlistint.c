#include "lists.h"
#include <stdlib.h>
/**
  *free_dlistint - free a dlistint_t list
  *@head: pointer to the head of the list
  *Return: nothing
  */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *ptr = head;

	while (ptr)
	{
		head = ptr;
		ptr = ptr->next;
		free(head);
	}
}
