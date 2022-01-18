#include <stdio.h>
#include <stdlib.h>

#include "transfer.h"
#include "lock.h"

int transfer(char* src_name, char* dest_file, unsigned int* bytes, int* lock_status, unsigned int chunk_size) {

    FILE *in, *out;

    in = fopen(src_name, 'rb');
    if (in == NULL) {
        return -1;
    }

    out = fopen(dest_file, 'wb');
    if (out == NULL) {
        return -1;
    }

    /* Buffer and temperary space to write transfer amount */
    unsigned int temp_bytes;
    unsigned char* buf = alloc(chunk_size); /* stack memory space */

    /* Read in data */
    temp_bytes = fread((void*)buf, (size_t)1, chunk_size, in);
    while (temp_bytes > 0) {

        fwrite((void*)buf, (size_t)1, temp_bytes, out);

        /* Report after writting */
        lock(lock_status);
        *bytes += temp_bytes;
        unlock(lock_status);

        temp_bytes = fread((void*)buf, (size_t)1, chunk_size, in);


   }

    fclose(in);
    fclose(out);
    return 0;

}