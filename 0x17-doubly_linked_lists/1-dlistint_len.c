#include "lists.h"
#include <stdio.h>
/**
  *dlistint_len - print the count of elements of a dlistint_t list
  *@h: pointer to the head of the list
  *Return: return the count of nodes in the list
  */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t n = 0;

	while (ptr)
	{
		n++;
		ptr = ptr->next;
	}
	return (n);
}
