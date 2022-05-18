?/ KEVIN FERNANDEZ
#include <stdio.h>
#include <stdlib.h>

struct BST {
    int val;
    struct BST *left;
    struct BST *right;
};

struct BST *MakeBSTNode(int v) {
    struct BST *bst;
    bst = malloc(sizeof(struct BST));
    bst->val = v;
    bst->left = NULL;
    bst->right = NULL;
    return bst;
};

void BSTInsert (struct BST *bst, int v) {
    if (v >= bst->val) {
        if (bst->right == NULL) {
            struct BST *newRight;
            newRight = malloc(sizeof(struct BST));
            newRight->val= v;
            newRight->left = NULL;
            newRight->right = NULL;
            bst->right = newRight;
        }
        else BSTInsert(bst->right, v);
    }
    else {
        if (bst->left == NULL) {
            struct BST *newLeft;
            newLeft = malloc(sizeof(struct BST));
            newLeft->val = v;
            newLeft->left = NULL;
            newLeft->right = NULL;
            bst->left = newLeft;
        }
        else BSTInsert(bst->left, v);
    }
}

void inOrderPrint(struct BST *bst) {
    if (bst != NULL){
        inOrderPrint(bst->left);
        printf("%d,", bst->val);
        inOrderPrint(bst->right);
    }
}

int main()
{
    // To test
    struct BST *myTree = MakeBSTNode(60);
    BSTInsert(myTree, 30);
    BSTInsert(myTree, 400);
    BSTInsert(myTree, 35);
    BSTInsert(myTree, 21);
    BSTInsert(myTree, 4565);

    inOrderPrint(myTree);
    printf("\none");
    return 0;
}
