#include "lists.h"

#include <stdio.h>
#include <stdlib.h>

/* Definition of a node in the linked list */
typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(listint_t** head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1;  // Empty list or single element list is considered a palindrome
    }

    // Find the middle of the linked list using the two-pointer technique
    listint_t* slow = *head;
    listint_t* fast = *head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    listint_t* prev = NULL;
    listint_t* current = slow->next;
    listint_t* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    // Compare the first half with the reversed second half of the linked list
    listint_t* first = *head;
    listint_t* second = prev;
    while (second != NULL) {
        if (first->data != second->data) {
            return 0;  // Not a palindrome
        }
        first = first->next;
        second = second->next;
    }

    return 1;  // Palindrome
}

int main() {
    // Test the is_palindrome function

    // Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
    listint_t* head = (listint_t*)malloc(sizeof(listint_t));
    head->data = 1;
    head->next = (listint_t*)malloc(sizeof(listint_t));
    head->next->data = 2;
    head->next->next = (listint_t*)malloc(sizeof(listint_t));
    head->next->next->data = 3;
    head->next->next->next = (listint_t*)malloc(sizeof(listint_t));
    head->next->next->next->data = 2;
    head->next->next->next->next = (listint_t*)malloc(sizeof(listint_t));
    head->next->next->next->next->data = 1;
    head->next->next->next->next->next = NULL;

    int result = is_palindrome(&head);
    printf("Is palindrome? %d\n", result);  // Output: Is palindrome? 1

    // Free the memory allocated for the linked list
    listint_t* current = head;
    listint_t* next = NULL;
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    return 0;
}

