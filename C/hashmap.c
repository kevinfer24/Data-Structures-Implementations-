#include <stdio.h>
#include <stdlib.h>

typedef struct List {
    int value;
    struct List *tail;
} List;

List *ListNode (int val) {
    List *list = malloc(sizeof(List));
    list->value = val;
    list->tail = NULL;
    return list;
}

typedef struct HMap {
    List *hashMap[10];
} HMap;

HMap *newHMap () {
    HMap *hm = malloc(sizeof(HMap));
    return hm;
}

void hashAndInsert (HMap *m, int x) {
    int hash = x % 10;
    if (m->hashMap[hash] == NULL) {
        m->hashMap[hash] = ListNode(x);
    }
    else {
        List *lst = ListNode(x);
        lst->tail = m->hashMap[hash];
        m->hashMap[hash] = lst;
    }
}

int main(int argc, char* argv[]){
    HMap *myMap = newHMap();
    hashAndInsert(myMap, 100);
    printf("%d\n", myMap->hashMap[0]->value);
    hashAndInsert(myMap, 30);
    printf("%d\n", myMap->hashMap[0]->value);
    printf("%d\n", myMap->hashMap[0]->tail->value);
}
