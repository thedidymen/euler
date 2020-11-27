/*
euler problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/


#include <iostream>

using namespace std;

int main() 
{
	int multi3 = 0;
	int multi5 = 0;
	int sumofmultis = 0;
	int upperlimit = 1000;

	while (multi3 < upperlimit || multi5 < upperlimit)
	{
		if (multi3 <= multi5)
		{
			multi3 += 3;
			if (multi3 < upperlimit && multi3 != multi5) 
				sumofmultis += multi3;
		}
		else if (multi5 < multi3)
		{
			multi5 += 5;
			if (multi5 < upperlimit && multi3 != multi5) 
				sumofmultis += multi5;
		}
		else 
		{
			cout << "Error, Abort!\n";
			break;
		}
	} 

	cout << "sum of multiples of 3 and 5 below " << upperlimit << " is: " << sumofmultis << '\n';
}