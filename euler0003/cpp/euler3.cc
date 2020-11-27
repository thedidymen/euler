/*
Euler 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

using namespace std;

void prime (long int n, vector<long int>& primenumbers);
void prime2 (long int n, vector<long int>& primenumbers2);
void factors (long int n, vector<long int>& primenumbers, vector<long int>& nfactorized);
void printvector (vector<long int>& printintvector);

int main() 
{
	long int n = 600851475143;
	vector<long int> primenumbers = {2, 3};
	vector<long int> primenumbers2 = {2, 3};
	vector<long int> nfactorized;

	auto start = chrono::steady_clock::now();
	prime(((long int) ceil(sqrt(n))), primenumbers);
	factors(n, primenumbers, nfactorized);
	auto end = chrono::steady_clock::now();

	cout << "[Prime(sqrt(n), factors(n), " << n << "]: " << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " MS" << endl;
	printvector(nfactorized);
	//printvector(primenumbers2);
}

void prime (long int n, vector<long int>& primenumbers)
// adds primenumbers upto n in vector primenumbers
{
	for (int currentnumber = primenumbers.back()+2; currentnumber < n; currentnumber += 2)
	{
		for (vector<long int>::iterator it = primenumbers.begin(); it != primenumbers.end(); ++it)
		{
			if (currentnumber % *it == 0)
			{
				break;
			}
			else if (*it >= ((long int) ceil(sqrt(currentnumber))))
			{
				primenumbers.emplace_back(currentnumber);
				break;
			}
		}

	}
}

void factors (long int n, vector<long int>& primenumbers, vector<long int>& nfactorized)
// adds primefactors of n in nfactorized
{
	long int remainder = n;
	for (vector<long int>::iterator it = primenumbers.begin(); it != primenumbers.end(); ++it)
	{
		while (remainder % *it == 0)
		{
			remainder /= *it;
			nfactorized.emplace_back(*it);
		}
		if (remainder <= 1)
			break;
	}
}

void printvector (vector<long int>& printintvector)
{
	for (std::vector<long int>::iterator it = printintvector.begin(); it != printintvector.end(); ++it)
	{
		cout << *it << ' ';
	}
	cout << endl;
}
