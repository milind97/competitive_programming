#include<iostream>
using namespace std;
int main()
{
	long int  x, num;
	unsigned long int y, n, mod;
	cin>>n;
	mod = 1000000007;
	if(n<=2)
	{
		cout<<0<<endl;
	}
	else
	{
		y = n-1;
        num = 1;
        x = 2;
        while(y > 0)
        {
            if(y % 2 == 1)
            {
                num = (num*x) % mod;
            }
            x = (x*x)%mod;
            y = y/2;
        }
        num = num + mod - 2;
        num = num % mod;
        cout<<num<<endl;
     }
     return 0;
}
	
