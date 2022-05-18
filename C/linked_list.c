// KEVIN FERNANDEZ
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int head;
    struct ListNode *tail;
};

struct ListNode *MakeList (int nums[], int length) {
    int i = length - 1;
    struct ListNode *listP = NULL;
    while (i >= 0) {
        struct ListNode *list;
        list = malloc(sizeof(struct ListNode));
        list->head = nums[i];
        list->tail = listP;
        listP = list;
        i -= 1;
    }
    return listP;
}

void printList(struct ListNode *LN) {
    struct ListNode *p = LN;
    while (p != NULL) {
        printf("%d,", p->head);
        p = p->tail;
    }

}

struct ListNode *ReverseList (struct ListNode *LN) {
    struct ListNode *p = LN;
    struct ListNode *cont = LN;
    struct ListNode *emp = NULL;

    while (p != NULL) {
        cont = cont->tail;
        p->tail  = emp;
        emp = p;
        p = cont;
    }
    return emp;

};

int main()
{
    // To test
    int numbers[] = {4,5,6,7,8,555,323,233,222,111,333,456};
    struct ListNode *list1 = MakeList(numbers, sizeof(numbers)/ sizeof(numbers[0]));
    printList(list1);
    

    list1 = ReverseList(list1);
    printList(list1);
    printf("\n");
    
    return 0;
}
