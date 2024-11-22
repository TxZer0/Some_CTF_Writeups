#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char** argv){
    if(strstr(argv[1],"\\")){
        printf("\"%s\" have \\ \n",argv[1]);
    }  
    system(argv[1]);
}
