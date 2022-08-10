#include <stdio.h>


int main(int argc, char** argv)
{
	char buffer[0xffff] = {'\0'};
	sprintf(buffer, "cp %s.hdl %s.cmp %s.tst /home/user/Desktop/nand2tetris/tools", argv[1], argv[1], argv[1]);
	system(buffer);
	printf("all files have been copied to -> /home/user/Desktop/nand2tetris/tools\n");
	return 0;
}

