#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t, maxr=0, i, l, r;
	cin>>t;
	int store[t][2];
	for(i=0;i<t;i++)
	{
		cin>>l>>r;
		store[i][0] = l;
		store[i][1] = r;
		if(r > maxr)
		{
			maxr = r;
		}
	}
	//cout<<maxr<<endl;
	int maxval = maxr + 1;
	vector<long >isprime(maxval , true);
	vector<long >prime;
	vector<long >SPF(maxval);
	isprime[0] = isprime[1] = false ;
    for (long int i=2; i<maxval ; i++)
    {
        if (isprime[i])
        {
         
            prime.push_back(i);
 
           
            SPF[i] = i;
        }
 
      
        for (long int j=0;
             j < (int)prime.size() &&
             i*prime[j] < maxval && prime[j] <= SPF[i];
             j++)
        {
            isprime[i*prime[j]]=false;
 
            SPF[i*prime[j]] = prime[j] ;
        }
    }
    flush(cout);
    cout<<"";
    cin.clear();
    int till_now[maxval];
    till_now[0] = 0;
    till_now[1] = 0;    
	int finalv[maxval];
	finalv[0] = 0;
	finalv[1] = 0;
	for(i=0;i<maxval;i++)
	{
    	if (isprime[i] == true)
    	{
    		till_now[i] = till_now[i-1] + 1;
    	}
    	else
    	{
        	till_now[i] = till_now[i-1];
        }
    	if(isprime[till_now[i]] == true)
    	{
        	finalv[i] = finalv[i-1] + 1;
        }
    	else
    	{
        	finalv[i] = finalv[i-1];
        }
	}
	for(i=0;i<t;i++)
	{
		cout<<finalv[store[i][1]] - finalv[store[i][0] - 1]<<endl;
	}
	
	return 0;
}
	
