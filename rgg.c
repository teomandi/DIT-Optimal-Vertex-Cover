#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
   FILE *fp;
   fp = fopen("graph.txt", "w+");
   int i, j, nnodes = 10, density = 50, seed;
   seed = (unsigned int) time(NULL);
   if (argc > 1)
      nnodes = atoi(argv[1]);
   if (argc > 2)
      density = atoi(argv[2]);
   if (argc > 3)
      seed = (unsigned int) atoi(argv[3]);
   srand(seed);
   printf("nodes: %d | density: %d\n", nnodes, density);
   for (i = 1 ; i < nnodes ; i++)
      for (j = i+1 ; j <= nnodes ; j++)
         if ((rand() % 100 + 1) <= density){
            printf("%d %d \n", i, j);
        	fprintf(fp,"%d %d \n", i, j);
    	}
    fclose(fp);
   return 0;
}
