#include<stdio.h>
#define SIZE 10
int display(int array[]){
	for(int i=0;i<SIZE;i++){
        printf("%d \t", array[i]);
		}
    printf("\n");
}

int find(int array[]){
	int X;
	printf("Enter value of X to find:\n");
	scanf("%d",&X);
	for(int i=0;i<SIZE;i++){
		if(array[i]==X){
			printf("At %d",i);
		}
	}
}

int smallest(int array[]){
    int small=array[0];
    for(int i=0;i<SIZE;i++){
        if(array[i]<small){
            small=array[i];
        }
    }
    printf("\nSmallest value: %d \n",small);
}
void average(int array[]){
	int sum=0;
	for(int i=0;i<SIZE;i++){
		sum+=array[i];
	}
	printf("\n average=%d\n",sum/10);
}

int multiplyN(int array[]){
    int	N;
    printf("Enter value for N: \n");
    scanf("%d",&N);
    
    for(int i=0;i<SIZE;i++){
    	array[i]=array[i]*N;
	}
}
void main(){
    int a[10];
    int n;
    
    printf("Enter the number of values\n");
    scanf("%d",&n);
    
    for(int i=0;i<n;i++){
        printf("Enter value of %d:\n",i+1);
        scanf("%d",&a[i]);
    }

    printf("Values entered= \n");

    for(int i=0;i<n;i++){
        printf("%d \t",a[i]);
    }
    
    smallest(a);
    average(a);
    multiplyN(a);
    display(a);
    find(a);

}