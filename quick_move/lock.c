#include "lock.h"

void lock(int* lock) {

    *lock = 1;
    return;

}

void unlock(int* lock) {

    *lock = 0;
    return;

}
