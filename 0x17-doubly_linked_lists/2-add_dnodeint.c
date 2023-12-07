#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
  *add_dnodeint - adds a new node at the beginning of dlistint_t list
  *@head: pointer to the head of the list
  *@n: number to add to the list
  *Return: return the address of the new node
  */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *ptr;

	ptr = malloc(sizeof(dlistint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = n;
	ptr->prev = NULL;
	ptr->next = *head;
	*head = ptr;
	return (ptr);
}
