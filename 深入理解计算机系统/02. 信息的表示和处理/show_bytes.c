#include <stdio.h>

typedef unsigned char* byte_pointer;

// 显示字节
void show_byte(byte_pointer start, size_t len)
{
	size_t i;
	for (i = 0; i < len; i++)
		printf(" %.2x", start[i]);
	printf("\n");
}

// int类型
void show_int(int x)
{
	show_byte((byte_pointer) &x, sizeof(int));
}

// 浮点类型
void show_float(float x)
{
	show_byte((byte_pointer) &x, sizeof(float));
}

// double类型
void show_double(double x)
{
	show_byte((byte_pointer) &x, sizeof(double));
}

// 其他类型
void show_point(void* x)
{
	show_byte((byte_pointer) &x, sizeof(void*));
}

int main()
{
	int x = 0x999908;
	show_int(x);
	show_float(x);
	show_point(&x);
	double y = 45456.45615157899;
	show_double(y);

	return 0;
}
