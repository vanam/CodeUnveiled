












































// g = gcd(a, b)

// a = x * g
// b = y * g

//                   a * b     x * g * y * g
// l = lcm(a, b) = --------- = ------------- = x * y * g
//                 gcd(a, b)         g

// g | a
// g | b

// a | l
// b | l

// => g | l



// ---------------- //
// Problem solution //
// ---------------- //

// Check if g | l

// x = 1                    => a = g

//     a * b   g * b
// l = ----- = ----- = b    => b = l
//       g       g


























#include <iostream>

using namespace std;

int main( int argc, char *argv[] ) {
    int tc;
    cin >> tc;
    while(tc--) {
        int g , l;
        cin >> g >> l;

        if (l % g == 0) { // solution exists if g | l
            cout << g << " " << l << "\n";
        } else {
            cout << "-1\n";
        }
    }

    exit(0);
}
// 0.000s #4331