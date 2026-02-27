#include<iostream>
#include<cmath>
using namespace std;
// Analysis of a first or second degree equation
int main()
{
    float a, b, c, d, x1, x2, x;
    cout << "Analysis of a first or second degree equation" << endl;
    cout << "Enter a, b, c: " << endl;
    cin >> a >> b >> c;

    if(a != 0)
    {
        cout << "Second degree equation" << endl;
        d = pow(b, 2) - 4 * a * c;

        if(d > 0)
        {
            cout << "There are 2 real solutions" << endl;
            x1 = (-b - sqrt(d)) / (2 * a);
            x2 = (-b + sqrt(d)) / (2 * a);
            cout << "The solutions are: " << x1 << " and " << x2 << endl;
        }
        else if(d == 0)
        {
            cout << "The solutions are coincident" << endl;
            x1 = (-b) / (2 * a);
            cout << "The solution is: " << x1 << endl;
        }
        else
        {
            cout << "The solutions are not real (complex numbers)" << endl;
        }
    }
    else
    {
        cout << "The equation is of the first degree" << endl;

        if(b != 0)
        {
            x = -c / b;
            cout << "The solution is: " << x << endl;
        }
        else
        {
            if(c == 0)
            {
                cout << "There are infinite solutions" << endl;
            }
            else
            {
                cout << "There is no solution" << endl;
            }
        }
    }
    return 0;
}