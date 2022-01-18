#ifndef TRANSFER_H
#define TRANSFER_H

int transfer(char* src_name, char* dest_file, unsigned int* bytes, int* lock, unsigned int chunk_size);

#endif /* TRANSFER_H */