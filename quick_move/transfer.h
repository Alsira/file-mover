#ifndef TRANSFER_H
#define TRANSFER_H

#include "header.h"

/**
 * @brief This copies a src file to a dest file
 * 
 * @param src_name Source file name
 * @param dest_file Destination file name
 * @param bytes The pointer to the number of bytes transfered
 * @param mutex The mutex lock
 * @param chunk_size The amount to read at once
 * @return int The amount transfered
 */
int transfer(char* src_name, char* dest_file, unsigned int* bytes, pthread_mutex_t mutex, unsigned int chunk_size);

#endif /* TRANSFER_H */