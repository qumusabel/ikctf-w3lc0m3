#include <stdio.h>
#include <string.h>

int main(){
	char* comm, exec;
	printf("Enter the passphrase (note: flag is in /flag.txt): ");
	scanf(%s, &comm);

	if (strlen(&comm) > 64){
		&exec = memcpy(&exec, &comm[64], strlen(&comm) - 64);
		system(exec);
	} else {
		printf("Wrong password!!!!!");
	}

	return 0;
}