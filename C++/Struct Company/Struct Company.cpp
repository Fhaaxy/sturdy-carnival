#include <iostream>
#define N 15
using namespace std;
struct Company {
    string name;
    string role;
    int id;
    float salary;
};
int main()
{
   Company employee[N], temp;
   int i, j, index = 0;
   float sum = 0, avg,  max, min;

   for(i=0;i<N;i++)
   {
       cout<<"Enter details of employer "<<i+1<<endl;
       cout<<"Name: ";
       cin>>employee[i].name;
       cout<<"Role: ";
       cin>>employee[i].role;
       cout<<"ID: ";
       cin>>employee[i].id;
       cout<<"Salary: ";
       cin>>employee[i].salary;
   }

   for(j = 0; j < N-1; j++)
   {
       for(i = 0; i < N-1; i++)
       {
           if(employee[i].salary < employee[i+1].salary)
           {
               temp = employee[i];
               employee[i] = employee[i+1];
               employee[i+1] = temp;
           }
       }
   }

   cout << "Employers sorted by descending salary" << endl;
   for(i = 0; i < N; i++)
   {
       cout << "Employer " << i + 1 << endl;
       cout << "Name: " << employee[i].name << endl;
       cout << "Role: " << employee[i].role << endl;
       cout << "ID: " << employee[i].id << endl;
       cout << "Salary: " << employee[i].salary << endl;
   }

   for(i = 0; i < N; i++)
   {
       sum = sum + employee[i].salary;
   }
   avg = sum / N;
   cout << "Average salary of employers: " << avg << endl;

   max = employee[0].salary;
   for(i = 1; i < N; i++)
   {
       if(employee[i].salary > max)
       {
           max = employee[i].salary;
           index = i;
       }
   }
   cout << "Highest-paid employee: " << employee[index].name << endl;
   cout << "Salary: " << max << endl;
  
   min = employee[0].salary;
   for(i = 1; i < N; i++)
   {
       if(employee[i].salary < min)
       {
           min = employee[i].salary;
           index = i;
       }
   }
   cout << "Lowest-paid employee: " << employee[index].name << endl;
   cout << "Salary: " << min << endl;
   return 0;
}