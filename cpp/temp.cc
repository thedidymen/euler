#include <iostream>

int main()
{
	int a = 1;
	a += a += 1;
	std::cout << a;
}