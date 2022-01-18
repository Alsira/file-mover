#include "transfer.h"

int transfer(char* src_name, char* dest_file, unsigned int* bytes, pthread_mutex_t mutex, unsigned int chunk_size) {

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
    size_t temp_bytes;
    unsigned char* buf = alloc(chunk_size); /* stack memory space */

    /* Read in data */
    size_t amount_read = fread((void*)buf, (size_t)1, chunk_size, in);
    while (temp_bytes > 0) {

        temp_bytes = fwrite((void*)buf, (size_t)1, amount_read, out);

        /* Report after writting */
        pthread_mutex_lock(mutex);
        *bytes += temp_bytes;
        pthread_mutex_unlock(mutex);

        temp_bytes = fread((void*)buf, (size_t)1, chunk_size, in);

   }

    fclose(in);
    fclose(out);
    return 0;

}