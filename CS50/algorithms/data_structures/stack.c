#include <stdio.h>

#define CAPACITY 5

typedef struct
{
    int elements[CAPACITY];
    int occupied_size;
}
stack;

void push(stack *s, int element);
int pop(stack *s);

int main(void)
{
    stack elements;
    elements.occupied_size = 0;

    // Print the stack
    printf("---\n");
    for (int i = 0; i < CAPACITY; i++)
    {
        printf("| |\n");
    }
    printf("\n\n");

    // Populate the stack
    int element;
    printf("--- Elements to be added ---\n");
    while (scanf("%i", &element) && element != 0)
    {
        if (elements.occupied_size >= CAPACITY)
        {
            printf("Capacity of the stack is full\n");
            break;
        }

        push(&elements, element);
        printf("There are currently %i elements in the stack\n\n", elements.occupied_size);
    }

    // Print the stack
    printf("---\n");
    for (int i = 0; i < elements.occupied_size; i++)
    {
        printf("|%i|\n", elements.elements[i]);
    }
    for (int i = elements.occupied_size; i < CAPACITY; i++)
    {
        printf("|  |\n");
    }
    printf("\n\n");

    // Empty the stack
    printf("--- Element to be popped ---\n");

    while (elements.occupied_size != 0)
    {
        int e = pop(&elements);
        printf("Element popped: %i\n", e);
        printf("There are still %i elements in the stack\n\n", elements.occupied_size);

        printf("---\n");
        for (int i = 0; i < elements.occupied_size; i++)
        {
            printf("|%i|\n", elements.elements[i]);
        }
        for (int i = elements.occupied_size; i < CAPACITY; i++)
        {
            printf("| |\n");
        }
        printf("\n\n");
    }
}

void push(stack *s, int element)
{
    s->elements[s->occupied_size] = element;
    s->occupied_size++;
}

int pop(stack *s)
{
    int element = s->elements[s->occupied_size - 1];
    s->occupied_size--;
    return element;
}