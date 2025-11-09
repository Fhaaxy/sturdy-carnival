#include <iostream>
#define C 2
#define R 2
using namespace std;
int main()
{
    cout << "Cramer Solver" << endl;
    int A[C][R], c[C], i, j;
    float D, Dx, Dy, x, y;

    cout << "Enter the elements of the coefficient matrix (2x2):" << endl;
    for (i = 0; i < C; i++)
    {
        cout << "Equation " << i + 1 << ":" << endl;
        for (j = 0; j < R; j++)
        {
            cout << "Enter coefficient [" << i << "][" << j << "]: ";
            cin >> A[i][j];
        }

        cout << "Enter constant term[" << i << "]: ";
        cin >> c[i];
    }

    for (i = 0; i < C; i++)
    {
        cout << "Equation " << i + 1 << ": ";
        for (j = 0; j < R; j++)
        {
            cout << A[i][j] << " ";
        }
        cout << "= " << c[i] << endl;
    }

    D = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0]);
    Dx = (c[0] * A[1][1]) - (A[0][1] * c[1]);
    Dy = (A[0][0] * c[1]) - (c[0] * A[1][0]);

    x = Dx / D;
    y = Dy / D; 

    cout << "The solution is:" << endl;
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
    return 0;
}