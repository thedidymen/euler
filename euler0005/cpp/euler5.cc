


#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

using namespace std;

void prime (long int n, vector<long int>& primenumbers);
void prime2 (long int n, vector<long int>& primenumbers2);
vector<long int> factors (long int n, vector<long int>& primenumbers);
void printvector (vector<long int>& printintvector);

int main() 
{
	long int n;
	vector<long int> primenumbers = {2, 3};
	vector<long int> nfactorized;

	auto start = chrono::steady_clock::now();

	for (long int n = 1; n < 21; n++)
	{
		vector<long int> nfactorized;
		nfactorized = factors(n, primenumbers);
		cout << n << endl;
		printvector(nfactorized);
		cout << endl;
	}

	auto end = chrono::steady_clock::now();
	cout << "[Prime(sqrt(n), factors(n), " << n << "]: " << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " MS" << endl;
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

vector<long int> factors (long int n, vector<long int>& primenumbers)
// adds primefactors of n in nfactorized
{
	prime(((long int) ceil(sqrt(n))), primenumbers);
	vector<long int> nfactorized;
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
	return nfactorized;
}

void printvector (vector<long int>& printintvector)
{
	for (std::vector<long int>::iterator it = printintvector.begin(); it != printintvector.end(); ++it)
	{
		cout << *it << ' ';
	}
	cout << endl;
}
