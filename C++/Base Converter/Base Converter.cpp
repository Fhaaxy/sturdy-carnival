#include <iostream>
#include <cmath>
#define N 16
using namespace std;

//Decimal to Binary 
void decimalToBinary(int num) {
    int bin[N], i = 0;

    if (num < pow(2, N)) {
        do {
            bin[i] = num % 2;
            num = num / 2;
            i++;
        } while (num > 0);

        cout << "Binary: ";
        for (i = i - 1; i >= 0; i--)
            cout << bin[i];
        cout << endl;
    } else {
        cout << "Error: number too large." << endl;
    }
}

//Decimal to Octal
void decimalToOctal(int num) {
    int ott[N], i = 0;

    if (num < pow(8, N)) {
        do {
            ott[i] = num % 8;
            num = num / 8;
            i++;
        } while (num > 0);

        cout << "Octal: ";
        for (i = i - 1; i >= 0; i--)
            cout << ott[i];
        cout << endl;
    } else {
        cout << "Error: number too large." << endl;
    }
}

//Decimal to Hexadecimal
void decimalToHex(int num) {
    char esa[N];
    int resto, i = 0;

    if (num < pow(16, N)) {
        do {
            resto = num % 16;
            switch (resto) {
                case 10: esa[i] = 'A'; break;
                case 11: esa[i] = 'B'; break;
                case 12: esa[i] = 'C'; break;
                case 13: esa[i] = 'D'; break;
                case 14: esa[i] = 'E'; break;
                case 15: esa[i] = 'F'; break;
                default: esa[i] = resto + '0'; break;
            }
            num = num / 16;
            i++;
        } while (num > 0);

        cout << "Hexadecimal: ";
        for (i = i - 1; i >= 0; i--)
            cout << esa[i];
        cout << endl;
    } else {
        cout << "Error: number too large." << endl;
    }
}

//Binary to Decimal
void binaryToDecimal() {
    int bin[N], i = 0, num = 0;

    cout << "Enter a binary number (" << N << " digits): " << endl;
    for (i = 0; i < N; i++) {
        cin >> bin[i];
        if (bin[i] != 0 && bin[i] != 1) {
            cout << "Error: invalid binary digit." << endl;
            return;
        }
    }

    for (i = 0; i < N; i++)
        num = num + bin[i] * pow(2, N - 1 - i);

    cout << "Decimal: " << num << endl;
}

//Octal to Decimal
void octalToDecimal() {
    int ott[N], i = 0, num = 0;

    cout << "Enter an octal number (" << N << " digits): " << endl;
    for (i = 0; i < N; i++) {
        cin >> ott[i];
        if (ott[i] < 0 || ott[i] > 7) {
            cout << "Error: invalid octal digit." << endl;
            return;
        }
    }

    for (i = 0; i < N; i++)
        num = num + ott[i] * pow(8, N - 1 - i);

    cout << "Decimal: " << num << endl;
}

//Hexadecimal to Decimal
void hexToDecimal() {
    char esa[N + 1];
    int i = 0, num = 0, digit, len = 0;

    cout << "Enter a hexadecimal number (e.g. 1F3A): " << endl;
    cin >> esa;

    while (esa[len] != '\0') len++;

    for (i = 0; i < len; i++) {
        char c = esa[i];
        if (c >= '0' && c <= '9')
            digit = c - '0';
        else if (c >= 'A' && c <= 'F')
            digit = c - 'A' + 10;
        else if (c >= 'a' && c <= 'f')
            digit = c - 'a' + 10;
        else {
            cout << "Error: invalid hexadecimal digit." << endl;
            return;
        }
        num = num + digit * pow(16, len - 1 - i);
    }

    cout << "Decimal: " << num << endl;
}

//Main
int main() {
    int choice;

    cout << "Choose a conversion:" << endl;
    cout << "1. Decimal -> Binary" << endl;
    cout << "2. Decimal -> Octal" << endl;
    cout << "3. Decimal -> Hexadecimal" << endl;
    cout << "4. Binary  -> Decimal" << endl;
    cout << "5. Octal   -> Decimal" << endl;
    cout << "6. Hexadecimal -> Decimal" << endl;
    cin >> choice;

    int num;

    switch (choice) {
        case 1:
            cout << "Enter a decimal number: " << endl;
            cin >> num;
            decimalToBinary(num);
            break;
        case 2:
            cout << "Enter a decimal number: " << endl;
            cin >> num;
            decimalToOctal(num);
            break;
        case 3:
            cout << "Enter a decimal number: " << endl;
            cin >> num;
            decimalToHex(num);
            break;
        case 4:
            binaryToDecimal();
            break;
        case 5:
            octalToDecimal();
            break;
        case 6:
            hexToDecimal();
            break;
        default:
            cout << "Error: invalid choice." << endl;
            break;
    }

    return 0;
}
