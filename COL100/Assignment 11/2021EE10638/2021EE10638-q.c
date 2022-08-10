#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Employee *Boss_helper(int);
int len();
int getitem(int);
int Boss(int);
int Level(int);
struct Employee *emp_helper(int);

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

// ASSIGNMENT 11

// The following is a employee in the organisation, it has the pointer to two more employees a subordinate_1 and a subordinate_2
struct Employee
{
    int emp_id; // emp_ids will be unique
    struct Employee *subordinate_1;
    struct Employee *subordinate_2;
};

struct get_details
{
    int level;
    struct Employee *boss;
    struct Employee *sub;
};

struct get_details *create_variable()
{
    struct get_details *ptr = malloc(sizeof(struct get_details));
    return ptr;
}

// The following function creates a employee and returns its pointer
struct Employee *create_employee(int x)
{
    struct Employee *ptr = (struct Employee *)malloc(sizeof(struct Employee));
    ptr->emp_id = x;
    ptr->subordinate_1 = NULL;
    ptr->subordinate_2 = NULL;
    return ptr;
}

// The following code creates a organisation from scanning the input file
struct Employee *create_company()
{
    int x;
    scanf("%d", &x);

    if (x == -1)
        return NULL; // -1 is used when there is a NULL pointer ie when no value is present
    struct Employee *par = create_employee(x);

    par->subordinate_1 = create_company();
    par->subordinate_2 = create_company();

    return par;
}

// The following function
void print_company_helper(struct Employee *ceo)
{
    // take input
    if (!ceo)
    {
        printf("%d ", -1);
        return;
    }
    printf("%d ", ceo->emp_id);
    print_company_helper(ceo->subordinate_1);
    print_company_helper(ceo->subordinate_2);
    return;
}

void get_employees_helper(struct Employee *ceo)
{
    // take input
    if (!ceo)
        return;
    printf("%d ", ceo->emp_id);
    get_employees_helper(ceo->subordinate_1);
    get_employees_helper(ceo->subordinate_2);
    return;
}

void print_company(struct Employee *ceo)
{
    print_company_helper(ceo);
    printf("\n");
    return;
}

void get_employee_details(int id, struct Employee *ceo, int level, struct get_details *ptr)
{
    if (ceo)
    {
        if (ceo->subordinate_1 && ceo->subordinate_1->emp_id == id)
        {
            ptr->boss = ceo;
            ptr->level = level + 1;
            ptr->sub = ceo->subordinate_1;
            return;
        }
        if (ceo->subordinate_2 && ceo->subordinate_2->emp_id == id)
        {
            ptr->boss = ceo;
            ptr->level = level + 1;
            ptr->sub = ceo->subordinate_2;
            return;
        }
        get_employee_details(id, ceo->subordinate_1, level + 1, ptr);
        get_employee_details(id, ceo->subordinate_2, level + 1, ptr);
    }
}

void get_level_helper(struct Employee *ceo, int level, int level_com)
{
    // take input
    if (!ceo)
        return;
    if (level == level_com)
        printf("%d ", ceo->emp_id);
    get_level_helper(ceo->subordinate_1, level + 1, level_com);
    get_level_helper(ceo->subordinate_2, level + 1, level_com);
    return;
}

void get_elements(struct Employee *ceo)
{
    if (ceo)
    {
        append(ceo->emp_id);
        get_elements(ceo->subordinate_1);
        get_elements(ceo->subordinate_2);
    }
}

void get_interns(struct Employee *ceo)
{
    if (ceo->subordinate_1 == NULL && ceo->subordinate_2 == NULL)
    {
        if (Level(Boss_helper(ceo->emp_id)->emp_id) == 0)
            append(ceo->emp_id);
        else if (Boss_helper(ceo->emp_id)->subordinate_1 == NULL || Boss_helper(ceo->emp_id)->subordinate_1 == ceo)
            append(ceo->emp_id);
    }
    else
    {
        if (ceo->subordinate_1)
            get_interns(ceo->subordinate_1);
        if (ceo->subordinate_2)
            get_interns(ceo->subordinate_2);
    }
}

struct Employee *iter_element(struct Employee *ceo, int id1, int id2)
{
    int l1 = Level(id1);
    int l2 = Level(id2);
    if (l1 == 0 || l2 == 0)
        return ceo;
    if (l1 > l2)
    {
        while (l1 != l2)
        {
            id1 = Boss(id1);
            l1--;
        }
    }
    if (l2 > l1)
    {
        while (l1 != l2)
        {
            id2 = Boss(id2);
            l2--;
        }
    }
    if (id1 == id2)
        return emp_helper(id1);
    while (Boss(id1) != Boss(id2))
    {
        id1 = Boss(id1);
        id2 = Boss(id2);
    }
    return Boss_helper(id1);
}

// --------------------------------------------------- YOU CAN EDIT BELOW THIS LINE -----------------------------------

struct Employee *CEO = NULL;
// CEO is a global pointer that points to the CEO of the company

/*  In this function you have to print all the employees at a given level, Note that ceo is at level 0
In any of the functions which involve printing you need not print -1 for NULL pointers */

struct Employee *Boss_helper(int emp_id)
{
    if (CEO->emp_id == emp_id)
        return CEO;
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    struct Employee *result;
    result = ptr->boss;
    free(ptr);
    return result;
}

struct Employee *emp_helper(int emp_id)
{
    if (CEO->emp_id == emp_id)
        return CEO;
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    struct Employee *result;
    result = ptr->sub;
    free(ptr);
    return result;
}

void EmployeesAtSameLevel(int level)
{
    get_level_helper(CEO, 0, level);
    return;
}

// You have to print the employees as you search the organization look for the examples in the pdf and the input.txt and output.txt for details
// Note: You do not have to print -1 for NULL pointers

void get_employees()
{
    get_employees_helper(CEO);
    return;
}

/* In the following function you have to print the immediate team of a employee - it includes their boss and their subordinates
Note: You do not have to print -1 for NULL pointers */

void ImmediateTeam(int emp_id)
{
    if (CEO->emp_id == emp_id)
    {
        if (CEO->subordinate_1)
            printf("%d ", CEO->subordinate_1->emp_id);
        if (CEO->subordinate_2)
            printf("%d ", CEO->subordinate_2->emp_id);
        return;
    }
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    printf("%d ", ptr->boss->emp_id);
    if (ptr->sub->subordinate_1)
        printf("%d ", ptr->sub->subordinate_1->emp_id);
    if (ptr->sub->subordinate_2)
        printf("%d ", ptr->sub->subordinate_2->emp_id);
    free(ptr);
    return;
}

// The following function returns the level of a employee with the given emp_id
int Level(int emp_id)
{
    if (CEO->emp_id == emp_id)
        return 0;
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    int result;
    result = ptr->level;
    free(ptr);
    return result;
}

// The following function gives the distance between employees with emp_id1 and emp_id2
int Distance(int emp_id1, int emp_id2)
{
    if (emp_id1 == emp_id2)
        return 0;
    struct Employee *ptr = iter_element(CEO, emp_id1, emp_id2);
    struct get_details *ptr1 = create_variable();
    struct get_details *ptr2 = create_variable();
    int a = 0;
    int b = 0;
    if ((ptr->emp_id == emp_id1))
        a = 0;
    else
    {
        get_employee_details(emp_id1, ptr, 0, ptr1);
        a = ptr1->level;
    }
    if ((ptr->emp_id == emp_id2))
        b = 0;
    else
    {
        get_employee_details(emp_id2, ptr, 0, ptr2);
        b = ptr2->level;
    }
    return a + b;
}

/* The following function takes an emp_id this will belong to a employee in the organisation and your task is to return the emp_id of its boss
Note: If the boss does not exit return -1 */
int Boss(int emp_id)
{
    if (CEO->emp_id == emp_id)
        return -1;
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    int result;
    result = ptr->boss->emp_id;
    free(ptr);
    return result;
}

/* The following function returns the diameter of a Organisation -
a diameter is the maximum distance between any two emp_ids in the organisation. You can use the distance function implemented above */
int dia = 0;
int Diameter()
{
    if (dia != 0)
        return dia;
    clear();
    get_interns(CEO);
    append(CEO->emp_id);
    int l = len();
    if (l == 1)
    {
        return 0;
    }
    int m = Distance(PythonListHead->data, PythonListHead->next->data);
    struct Node *cur = PythonListHead;
    for (int i = 0; i < l - 1; i++)
    {
        struct Node *cur2 = cur;
        for (int j = i + 1; j < l; j++)
        {
            cur2 = cur2->next;
            int d = Distance(cur->data, cur2->data);
            if (d > m)
                m = d;
        }
        cur = cur->next;
    }
    dia = m;
    return m;
}

/* The following function takes an emp_id of a employee and returns the number of employees directly connected to it.
NULL pointers are not included */

int TeamSize(int emp_id)
{
    int c = 0;
    if (CEO->emp_id == emp_id)
    {
        if (CEO->subordinate_1)
            c++;
        if (CEO->subordinate_2)
            c++;
        return c;
    }
    struct get_details *ptr = create_variable();
    get_employee_details(emp_id, CEO, 0, ptr);
    c++;
    if (ptr->sub->subordinate_1)
        c++;
    if (ptr->sub->subordinate_2)
        c++;
    free(ptr);
    return c;
}

// --------------------------------------------------- YOU CAN EDIT ABOVE THIS LINE -----------------------------------

/* The following driver code creates a organisation for you and based on the input file
it will call all the functions that are necessary, your job is to edit the functions
above the line. Their descriptions are in the pdf and in the comments in the code. */

int main(int argc, char const *argv[])
{
    CEO = create_company();
    print_company(CEO);

    int T;
    scanf("%d", &T);

    char operation_type[50];

    while (T--)
    {
        scanf("%s", operation_type);

        if (strcmp(operation_type, "level") == 0)
        {
            int x;
            scanf("%d", &x);
            int d = Level(x);
            printf("%d\n", d);
        }

        if (strcmp(operation_type, "distance") == 0)
        {
            int x, y;
            scanf("%d %d", &x, &y);
            int d = Distance(x, y);
            printf("%d\n", d);
        }

        if (strcmp(operation_type, "employees_at_same_level") == 0)
        {
            int x;
            scanf("%d", &x);
            EmployeesAtSameLevel(x);
            printf("\n");
        }

        if (strcmp(operation_type, "get_employees") == 0)
        {
            get_employees();
            printf("\n");
        }

        if (strcmp(operation_type, "boss") == 0)
        {
            int x;
            scanf("%d", &x);
            int d = Boss(x);
            printf("%d\n", d);
        }

        if (strcmp(operation_type, "diameter") == 0)
        {
            int d = Diameter();
            printf("%d\n", d);
        }

        if (strcmp(operation_type, "immediate_team") == 0)
        {
            int x;
            scanf("%d", &x);
            ImmediateTeam(x);
            printf("\n");
        }

        if (strcmp(operation_type, "team_size") == 0)
        {
            int x;
            scanf("%d", &x);
            int d = TeamSize(x);
            printf("%d\n", d);
        }
    }

    return 0;
}
