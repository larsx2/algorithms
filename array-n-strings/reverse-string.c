#include <stdio.h>
#include <string.h>

void reverse(char * s) {
    char tmp;
    int len = strlen(s);

    for (int i=0; i<len/2; i++) {
        tmp = s[i];
        s[i] = s[len-1-i];
        s[len-1-i] = tmp;
    }
}

int main() {
    char name[] = "Eduardo";
    printf("From '%s' ", name);
    reverse(name);
    printf("to '%s'", name);
}
