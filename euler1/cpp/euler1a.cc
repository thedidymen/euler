/*
euler problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/


#include <iostream>

using namespace std;

int sumofdivisors ( int divisor , int upperlimit );

int main()
{

	int upperlimit = 999;
	int sumofmultis = sumofdivisors(3, upperlimit) + sumofdivisors(5, upperlimit) - sumofdivisors(15, upperlimit);

	cout << "sum of multiples of 3 and 5 below " << (upperlimit+1)<< " is: " << sumofmultis << '\n';
}

int sumofdivisors ( int divisor , int upperlimit )
{
	int p = upperlimit / divisor;
	return divisor * ( p * (p + 1) ) / 2;
}