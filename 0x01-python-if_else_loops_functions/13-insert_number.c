#include "lists.h"

/**
 * Inserts a number into a singly-linked list in sorted order. singly-linked list.
 * @param head: A pointer to the head of the linked list.
 * @param number: The number to insert.
 * Author - Samuel Chigozie
 *@return: If the function fails - NULL. Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
