#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
  *add_dnodeint_end - adds a new node at the end of dlistint_t list
  *@head: pointer to the head of the list
  *@n: number to add to the list
  *Return: return the address of the new node
  */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *ptr;
	dlistint_t *h = *head;

	ptr = malloc(sizeof(dlistint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = n;
	ptr->next = NULL;
	if (*head == NULL)
	{
		ptr->prev = NULL;
		*head = ptr;
	}
	else
	{
		while (h->next)
		{
			h = h->next;
		}
		ptr->prev = h;
		h->next = ptr;
	}

	return (ptr);
}
