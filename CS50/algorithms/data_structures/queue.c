#include <stdio.h>

#define CAPACITY 5

typedef struct
{
    int elements[CAPACITY];
    int occupied_size;
    int first_element_position;
}
queue;

void enqueue(queue *s, int element);
int dequeue(queue *s);

int main(void)
{
    queue elements;
    elements.occupied_size = 0;
    elements.first_element_position = 0;

    // Print the queue
    printf("\n");
    for (int i = 0; i < CAPACITY * 2; i++)
    {
        printf("-");
    }
    printf("\n");
    for (int i = 0; i < CAPACITY * 2; i++)
    {
        printf(" ");
    }
    printf("\n");
    for (int i = 0; i < CAPACITY * 2; i++)
    {
        printf("-");
    }
    printf("\n\n");

    // Populate the queue
    int element;
    printf("--- Elements to be added ---\n");
    while (scanf("%i", &element) && element != 0)
    {
        if (elements.occupied_size >= CAPACITY)
        {
            printf("Capacity of the queue is full\n");
            break;
        }

        enqueue(&elements, element);
        printf("There are currently %i elements in the queue\n\n", elements.occupied_size);
    }

    // Print the queue
    for (int i = 0; i < CAPACITY * 2; i++)
    {
        printf("-");
    }
    printf("\n");
    for (int i = 0; i < elements.occupied_size; i++)
    {
        printf("%i ", elements.elements[i]);
    }
    for (int i = elements.occupied_size; i < CAPACITY; i++)
    {
        printf(" ");
    }
    printf("\n");
    for (int i = 0; i < CAPACITY * 2; i++)
    {
        printf("-");
    }
    printf("\n\n");

    // Empty the stack
    printf("--- Element to be popped ---\n");

    while (elements.occupied_size != 0)
    {
        int e = dequeue(&elements);
        printf("Element popped: %i\n", e);
        printf("There are still %i elements in the queue\n\n", elements.occupied_size);

        for (int i = 0; i < CAPACITY * 2; i++)
        {
            printf("-");
        }
        printf("\n");
        for (int i = elements.first_element_position; i < CAPACITY; i++)
        {
            printf("%i ", elements.elements[i]);
        }
        printf("\n");
        for (int i = 0; i < CAPACITY * 2; i++)
        {
            printf("-");
        }
        printf("\n\n");
    }
}

void enqueue(queue *s, int element)
{
    s->elements[s->occupied_size] = element;
    s->occupied_size++;
}

int dequeue(queue *s)
{
    int element = s->elements[s->first_element_position];
    s->occupied_size--;
    s->first_element_position++;
    return element;
}