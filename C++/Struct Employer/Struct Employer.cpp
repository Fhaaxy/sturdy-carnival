#include <iostream>
#define N 5
using namespace std;
struct Employer {
    string name;
    string role;
    int id;
    float salary;
};
int main()
{
   Employer company[N], temp;
   int i, j;
   float sum = 0, avg,  max, min;

   for(i=0;i<N;i++)
   {
       cout<<"Enter details of employer "<<i+1<<endl;
       cout<<"Name: ";
       cin>>company[i].name;
       cout<<"Role: ";
       cin>>company[i].role;
       cout<<"ID: ";
       cin>>company[i].id;
       cout<<"Salary: ";
       cin>>company[i].salary;
   }

for(j = 0; j < N-1; j++)
    {
        for(i = 0; i < N-1; i++)
        {
            if(company[i].salary < company[i+1].salary)
            {
                temp = company[i];
                company[i] = company[i+1];
                company[i+1] = temp;
            }
        }
    }

    cout << "Employers sorted by descending salary";
    for(i = 0; i < N; i++)
    {
        cout << "Employer " << i + 1 << endl;
        cout << "Name: " << company[i].name << endl;
        cout << "Role: " << company[i].role << endl;
        cout << "ID: " << company[i].id << endl;
        cout << "Salary: " << company[i].salary << endl;
    }

   for(i = 0; i < N; i++)
   {
       sum = sum + company[i].salary;
   }
   avg=sum/N;
   cout<<"Average salary of employers:"<<avg<<endl;

    max=company[0].salary;
    for(i = 1;i < N; i++)
    {
        if(company[i].salary > max)
        {
            max=company[i].salary;
        }
    }
    cout<<"Maximum salary: "<<max<<endl;
  
    min=company[0].salary;
    for(i = 1; i < N; i++)
    {
        if(company[i].salary < min)
        {
            min=company[i].salary;
        }
    }
    cout<<"Minimum salary: "<<min<<endl;
 
    return 0;
}