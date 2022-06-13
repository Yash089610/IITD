#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int len();
int getitem(int);
struct Node
{
    int data;
    struct Node *next;
};

// create a node with data as x
struct Node *create_node(int x)
{
    struct Node *ptr = malloc(sizeof(struct Node));
    ptr->next = NULL;
    ptr->data = x;
    return ptr;
}

// delete the node at `ptr` and free its memory
void delete_node(struct Node *ptr)
{
    free(ptr);
}

// ------------------------------ Node struct definition ends here ------------------------------

// Use this to operate on the list, this will always point at the head of the list.
struct Node *PythonListHead = NULL;

// prints the list in space seperated format
void print_list(struct Node *head)
{
    struct Node *cur = head;
    while (cur)
    {
        printf("%d ", cur->data);
        cur = cur->next;
    }
    printf("\n");
}

// Add an item to the end of the list
void append(int x)
{
    if (PythonListHead == NULL)
        PythonListHead = create_node(x);
    else
    {
        struct Node *cur = PythonListHead;
        for (int i = 1; i < len(); i++)
        {
            cur = cur->next;
        }
        cur->next = create_node(x);
    }
}

// Insert an item at a given position.
// The first argument is the index of the element before which to insert
// second argument is the value to insert at that position
// if the position does not exist, do nothing
void insert(int position, int x)
{
    if (len() != 0)
    {
        int l = len();
        if (position == 0)
        {
            struct Node *y = PythonListHead;
            PythonListHead = create_node(x);
            PythonListHead->next = y;
        }
        if (position <= (l - 1) && position != 0)
        {
            struct Node *y = create_node(x);
            struct Node *cur = PythonListHead;
            for (int i = 0; i < (position - 1); i++)
            {
                cur = cur->next;
            }
            struct Node *ptr = cur->next;
            cur->next = y;
            cur = y;
            cur->next = ptr;
        }
    }
}

// Remove the item at the end of the list
void pop()
{
    int l = len();
    if (PythonListHead != NULL)
        if (l != 1)
        {
            struct Node *cur = PythonListHead;
            for (int i = 0; i < (len() - 2); i++)
            {
                cur = cur->next;
            }
            delete_node(cur->next);
            cur->next = NULL;
        }
    if (l == 1)
    {
        delete_node(PythonListHead);
        PythonListHead = NULL;
    }
}

// Remove all items from the list
void clear()
{
    struct Node *cur = PythonListHead;
    int x = len();
    for (int i = 0; i < (x - 1); i++)
    {
        struct Node *ptr = cur;
        cur = cur->next;
        delete_node(ptr);
    }
    delete_node(cur);
    PythonListHead = NULL;
}

// Return the number of times x appears in the list.
int count(int x)
{
    int c = 0;
    for (int i = 0; i <= (len() - 1); i++)
    {
        if (getitem(i) == x)
            c++;
    }
    return c;
}

// Reverse the elements of the list in place.
// Make sure you change `PythonListHead` accordingly
void reverse()
{
    if (len() != 0 && len() != 1)
    {
        struct Node *cur = PythonListHead;
        struct Node *ptr2 = cur->next;
        int x = len();
        for (int i = 0; i < (x - 1); i++)
        {
            struct Node *ptr = cur;
            cur = ptr2;
            ptr2 = cur->next;
            cur->next = ptr;
        }
        PythonListHead->next = NULL;
        PythonListHead = cur;
    }
}

// Return the number of elements in the list
int len()
{
    int c = 0;
    struct Node *cur = PythonListHead;
    while (cur)
    {
        c++;
        cur = cur->next;
    }
    return c;
}

// Set the data attribute of the node at `position` to `x`
// if no such position, do nothing
void setitem(int position, int x)
{
    if (position < len() && PythonListHead != NULL)
    {
        struct Node *cur = PythonListHead;
        for (int i = 0; i < position; i++)
        {
            cur = cur->next;
        }
        cur->data = x;
    }
}

// Return the data of the node at `position`
// if no such position, return -1
int getitem(int position)
{
    if (position > (len() - 1))
        return -1;
    struct Node *cur = PythonListHead;
    for (int i = 0; i < position; i++)
    {
        cur = cur->next;
    }
    return cur->data;
}

// erase the node at position
// if no such position, do nothing
void erase(int position)
{
    int l = len();
    if (position == (l - 1))
    {
        pop();
        return;
    }
    if (position == 0 && PythonListHead != NULL)
    {
        PythonListHead = PythonListHead->next;
    }
    if (position < len() && position != 0)
    {
        struct Node *cur = PythonListHead;
        for (int i = 1; i < position; i++)
        {
            cur = cur->next;
        }
        struct Node *ptr = cur;
        cur = cur->next->next;
        delete_node(ptr->next);
        ptr->next = cur;
    }
}

// Returns a the head of the newly formed Python List
// containing elements present in positions in the original List.
// Note: you have to create new Python List and return its head.
// Here positions is an array of size n.
// eg. if positions = [2, 3, 5], you need to return a newly formed list
// having nodes that were at position 2, 3 and 5 in the original list.
// if there is such a position that is not present in the original list, do nothing
// with that position.
struct Node *index_into(int *positions, int n)
{
    int l = len();
    int j = 0;
    while (positions[j] >= l && j < n)
        j++;
    if (j == n)
        return NULL;
    struct Node *head = create_node(getitem(positions[j]));
    struct Node *cur = head;
    for (int i = (j + 1); i < n; i++)
    {
        if (positions[i] <= (l - 1))
        {
            cur->next = create_node(getitem(positions[i]));
            cur = cur->next;
        }
    }
    cur->next = NULL;
    return head;
}

// swaps the nodes present at `position` and `position+1`
// if either of  `position` or `position+1` does not exist, do nothing
void swap(int position)
{
    if (PythonListHead != NULL)
    {
        if (position <= (len() - 2) && position != 0)
        {
            struct Node *cur = PythonListHead;
            for (int i = 0; i < (position - 1); i++)
            {
                cur = cur->next;
            }
            struct Node *ptrold = cur;
            cur = cur->next;
            ptrold->next = cur->next;
            struct Node *ptr = cur->next->next;
            cur->next->next = cur;
            cur->next = ptr;
        }
        if (position == 0 && len() != 1)
        {
            struct Node *cur = PythonListHead;
            PythonListHead = cur->next;
            cur->next = PythonListHead->next;
            PythonListHead->next = cur;
        }
    }
}

// sort the Python list
// you may use the above defined swap function to
// implement bubble sort. But its upto you.
void sort()
{
    struct Node *cur = PythonListHead;
    for (int i = 0; i < (len() - 1); i++)
    {
        cur = PythonListHead;
        for (int j = 0; j < (len() - 1 - i); j++)
        {
            if ((cur->data) > (cur->next->data))
                swap(j);
            else
                cur = cur->next;
        }
    }
}

// ----------------------- Driver program starts here -----------------------

int main(int argc, char const *argv[])
{
    int T;
    scanf("%d", &T);

    char operation_type[20];
    int indices[100];

    while (T--)
    {
        scanf("%s", operation_type);

        if (strcmp(operation_type, "append") == 0)
        {
            int x;
            scanf("%d", &x);
            append(x);
        }

        if (strcmp(operation_type, "insert") == 0)
        {
            int pos, x;
            scanf("%d %d", &pos, &x);
            insert(pos, x);
        }

        if (strcmp(operation_type, "pop") == 0)
        {
            pop();
        }

        if (strcmp(operation_type, "clear") == 0)
        {
            clear();
        }

        if (strcmp(operation_type, "count") == 0)
        {
            int x;
            scanf("%d", &x);
            int cnt = count(x);
            printf("%d\n", cnt);
        }

        if (strcmp(operation_type, "reverse") == 0)
        {
            reverse();
        }

        if (strcmp(operation_type, "len") == 0)
        {
            int length = len();
            printf("%d\n", length);
        }

        if (strcmp(operation_type, "setitem") == 0)
        {
            int pos, x;
            scanf("%d %d", &pos, &x);
            setitem(pos, x);
        }

        if (strcmp(operation_type, "getitem") == 0)
        {
            int pos;
            scanf("%d", &pos);
            int value = getitem(pos);
            printf("%d\n", value);
        }

        if (strcmp(operation_type, "print") == 0)
        {
            print_list(PythonListHead);
        }

        if (strcmp(operation_type, "erase") == 0)
        {
            int pos;
            scanf("%d", &pos);
            erase(pos);
        }

        if (strcmp(operation_type, "swap") == 0)
        {
            int pos;
            scanf("%d", &pos);
            swap(pos);
        }

        if (strcmp(operation_type, "index_into") == 0)
        {
            int n;
            scanf("%d", &n);
            for (int i = 0; i < n; i++)
                scanf("%d", &indices[i]);
            struct Node *new_head = index_into(indices, n);
            print_list(new_head);
        }

        if (strcmp(operation_type, "sort") == 0)
        {
            sort();
        }
    }
}