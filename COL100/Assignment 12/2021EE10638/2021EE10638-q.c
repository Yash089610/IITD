#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Employee *Boss_helper(int);
int len();
struct Employee *getitem(int);
int Boss(int);
int Level(int);
struct Employee *emp_helper(int);

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

struct Node
{
    struct Employee *data;
    struct Node *next;
};

// create a node with data as x
struct Node *create_node(struct Employee *x)
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

// ------------------------------ Node struct definition ends here ------------------------------

// Use this to operate on the list, this will always point at the head of the list.
struct Node *PythonListHead = NULL;

// Add an item to the end of the list
void append(struct Employee *x)
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
        struct Node *cur = PythonListHead;
        PythonListHead = PythonListHead->next;
        delete_node(cur);
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

// Assignment 12
// The following is a employee in the organisation, it has the pointer to two more employees a subordinate_1 and a subordinate_2
struct Employee
{
    int emp_id; // emp_ids will be unique
    char *emp_name;
    int emp_salary;
    struct Employee *subordinate_1;
    struct Employee *subordinate_2;
};

// The following function creates a employee and returns its pointer
struct Employee *create_employee(int id, char *name, int salary)
{
    struct Employee *ptr = (struct Employee *)malloc(sizeof(struct Employee));
    ptr->emp_id = id;
    ptr->emp_salary = salary;
    ptr->emp_name = strdup(name);
    // strdup() creates a copy of the string or char pointer and stores it in the new char pointer of the employee
    ptr->subordinate_1 = NULL;
    ptr->subordinate_2 = NULL;
    return ptr;
}

// The following code creates a organisation from scanning the input file
struct Employee *create_company()
{
    int id, salary;
    char name[100];
    scanf("%d", &id);
    if (id == -1)
        return NULL; // -1 is used when there is a NULL pointer ie when no value is present

    scanf("%s %d", name, &salary);
    struct Employee *par = create_employee(id, name, salary);

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
    printf("%d %s %d ", ceo->emp_id, ceo->emp_name, ceo->emp_salary);
    print_company_helper(ceo->subordinate_1);
    print_company_helper(ceo->subordinate_2);
    return;
}

void print_company(struct Employee *ceo)
{
    print_company_helper(ceo);
    printf("\n");
    return;
}

void get_elements(struct Employee *ceo)
{
    if (ceo)
    {
        append(ceo);
        get_elements(ceo->subordinate_1);
        get_elements(ceo->subordinate_2);
    }
}

void same_lastname_helper(struct Employee *ceo, char *name)
{
    append(ceo);
    while (len() > 0)
    {
        struct Employee *cur = PythonListHead->data;
        if (cur->subordinate_1)
            append(cur->subordinate_1);
        if (cur->subordinate_2)
            append(cur->subordinate_2);
        if (strcmp(name, cur->emp_name) == 0)
            printf("%d ", cur->emp_id);
        erase(0);
    }
}

struct Employee *iter_element(struct Employee *ceo, int id1, int id2)
{
    int l1 = Level(id1);
    int l2 = Level(id2);

    if (id1 == id2 && ceo->emp_id == id1)
        return NULL;
    if (l1 == 0 || l2 == 0)
        return ceo;
    if (id1 == id2)
        return Boss_helper(id1);
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

// --------------------------------------------------- YOU CAN EDIT BELOW THIS LINE -----------------------------------

struct Employee *CEO = NULL;
// CEO is a global pointer that points to the CEO of the company

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

// The below function returns the employee id of the first common boss
int get_first_common_boss(int emp_id1, int emp_id2)
{
    struct Employee *ptr = iter_element(CEO, emp_id1, emp_id2);
    if (ptr)
        return ptr->emp_id;
    else
        return -1;
}

// Print the employees with the same last name sperated by a space in the order of their level
void same_last_names(int emp_id)
{
    clear();
    same_lastname_helper(CEO, emp_helper(emp_id)->emp_name);
    return;
}

// Print the bosses of the given employee in the order from CEO to immediate boss
void get_all_bosses(int emp_id)
{
    if (emp_id == CEO->emp_id)
    {
        printf("%d", -1);
        return;
    }
    clear();
    while (emp_id != CEO->emp_id)
    {
        append(Boss_helper(emp_id));
        emp_id = Boss(emp_id);
    }
    reverse();
    struct Node *cur = PythonListHead;
    for (int i = 0; i < len(); i++)
    {
        printf("%d ", cur->data->emp_id);
        cur = cur->next;
    }
    return;
}

// Return the average salary of the team with the given employee as head
double get_average_salary(int emp_id)
{
    clear();
    get_elements(emp_helper(emp_id));
    double c = 0.0;
    struct Node *cur = PythonListHead;
    for (int i = 0; i < len(); i++)
    {
        c += cur->data->emp_salary;
        cur = cur->next;
    }
    return c / len();
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

    char operation_type[100];

    while (T--)
    {
        scanf("%s", operation_type);

        if (strcmp(operation_type, "get_first_common_boss") == 0)
        {
            int x, y;
            scanf("%d %d", &x, &y);
            int ans = get_first_common_boss(x, y);
            printf("%d\n", ans);
        }
        else if (strcmp(operation_type, "same_last_names") == 0)
        {
            int x;
            scanf("%d", &x);
            same_last_names(x);
            printf("\n");
        }
        else if (strcmp(operation_type, "get_all_bosses") == 0)
        {
            int x;
            scanf("%d", &x);
            get_all_bosses(x);
            printf("\n");
        }
        else if (strcmp(operation_type, "get_average_salary") == 0)
        {
            int x;
            scanf("%d", &x);
            double ans = get_average_salary(x);
            printf("%.2f\n", ans);
        }
    }

    return 0;
}
