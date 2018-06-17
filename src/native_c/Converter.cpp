#define DLLEXPORT extern "C" __declspec(dllexport)
#include <stdio.h>
#include <ctype.h>

DLLEXPORT char* string_toupper(char array[]) {
   for (unsigned int i=0;array[i] != '\0';i++) {
        int is_lower = islower(array[i]);
        if (is_lower != 0) {
            array[i] = toupper(array[i]);
        }
   }

   return array;
}