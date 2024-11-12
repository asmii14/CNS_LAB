// #include <bits/stdc++.h> 
// using namespace std;

// // Function for extended Euclidean Algorithm 
// int gcdExtended(int a, int b, int *x, int *y) { 
//     // Base Case 
//     if (a == 0) 
//     { 
//         *x = 0; 
//         *y = 1; 
//         return b; 
//     } 
//     int x1, y1; // To store results of recursive call 
//     int gcd = gcdExtended(b%a, a, &x1, &y1); 
//     // Update x and y using results of 
//     // recursive call 
//     *x = y1 - (b/a) * x1; 
//     *y = x1; 
//     return gcd; 
// } 

// // Driver Code
// int main() { 
//     int x, y;
//     // a = 35, b = 15; 
//     int a,b;
//     cout<<"enter a and b:";
//     cin>>a>>b;
//     int g = gcdExtended(a, b, &x, &y); 
//     cout << "GCD(" << a << ", " << b << ") = " << g << endl;
//     return 0; 
// } 

#include <iostream>
using namespace std;

// Euclidean Algorithm to find GCD with intermediate steps
int EuclideanAlgorithm(int a, int b) {
    cout << "Euclidean Algorithm Steps: " << endl;
    int step = 1;
    while (b != 0) {
        int remainder = a % b;
        int quotient = a / b;
        cout << "Step " << step << ": " << a << " = " << b << " * " << quotient << " + " << remainder << endl;
        a = b;
        b = remainder;
        step++;
    }
    return a;
}

// Extended Euclidean Algorithm to find x, y with intermediate steps
int ExtendedEuclideanAlgorithm(int a, int b, int &x, int &y, int step = 1) {
    cout << "Extended Euclidean Algorithm Steps: " << endl;
    if (b == 0) {
        x = 1;
        y = 0;
        cout << "Step " << step << ": Base case reached, x = " << x << ", y = " << y << endl;
        return a;
    }
    
    int x1, y1;
    int gcd = ExtendedEuclideanAlgorithm(b, a % b, x1, y1, step + 1);
    
    // Update x and y using results of recursive call
    x = y1;
    y = x1 - (a / b) * y1;
    
    cout << "Step " << step << ": a = " << a << ", b = " << b << ", x = " << x << ", y = " << y << endl;
    return gcd;
}

int main() {
    int a, b;
    cout << "Enter two integers a and b: ";
    cin >> a >> b;

    // Euclidean Algorithm with intermediate steps
    int gcd = EuclideanAlgorithm(a, b);
    cout << "GCD of " << a << " and " << b << " is: " << gcd << endl;

    // Extended Euclidean Algorithm with intermediate steps
    int x, y;
    int extended_gcd = ExtendedEuclideanAlgorithm(a, b, x, y);
    cout << "The extended GCD is: " << extended_gcd << endl;
    cout << "The coefficients x and y are: " << x << ", " << y << endl;
    
    // Verifying: ax + by = GCD
    cout << "Verification: " << a << " * " << x << " + " << b << " * " << y << " = " << extended_gcd << endl;

    return 0;
}
