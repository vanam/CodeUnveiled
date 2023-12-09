
//   753
// - 491
// -----
//     2 (carry 0)


//   753
// - 491
// -----
//    62 (carry 1)


//   753
// - 491
// -----
//   262 (carry 0)

#include <string>            // Strings
#include <algorithm>         // Standard Template Library: Algorithms
#include <cstring>           // C Strings
#include <iostream>

using namespace std;

#define GOOGOLPLEX 10000 // enough to fit googol to the power of hundred (googolplex)

char tmp[GOOGOLPLEX]; // temp

string subtract(string a, string b) {
    int la = a.length();
    int lb = b.length();

    int sign = 1;
    if (la < lb || (la == lb && a.compare(b) < 0)) { // if a < b swap
        swap(a, b);
        swap(la, lb);
        sign = -1;
    }
    
    // char* tmp = new char[GOOGOL]; // this is not a corporate piece of code ;-)
    int carry = 0;

    for (int i = 0; i < la ; i++) {
        int ai = a[la - i - 1] - '0';
        int bi = i < lb ? b[lb - i - 1] - '0' : 0; // watch out for shorter b

        int v = ai - (bi + carry);

        if (v < 0) {
            v += 10;
            carry = 1;
        } else {
            carry = 0;
        }

        tmp[i] = '0' + (v % 10);
    }
    
    // terminate the string
    tmp[la] = '\0';    
    int lr = strlen(tmp);

    // remove trailing zeroes
    for (int i = lr - 1; i > 0; i--) {
        if (tmp[i] != '0') {
            break;
        }
        tmp[i] = '\0';
    }

    // add sign
    lr = strlen(tmp);
    if (sign < 0) {
        tmp[lr] = '-';
        tmp[lr + 1] = '\0';
    } else {
        tmp[lr] = '\0';
    }
    
    string result(tmp);
    // delete[] tmp;
    reverse(result.begin(), result.end());
    return result;
}

int main( int argc, char *argv[] )
{
    int tc;
    cin >> tc;
    while(tc--) {
        string a , b;
        cin >> a >> b;
        cout << subtract(a, b) << "\n";
    }

    exit(0);
}
// 0.000s #43    C++
// 0.170s #819   Python
// 0.560s #1019  Java