#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Function to calculate (base^exp) % mod
ll mod_exp(ll base, ll exp, ll mod) {
    ll result = 1;
    while (exp > 0) {
        if (exp % 2 == 1)
            result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Extended Euclidean Algorithm for modular inverse
ll mod_inverse(ll a, ll m) {
    ll m0 = m, t, q;
    ll x0 = 0, x1 = 1;

    if (m == 1)
        return 0;

    while (a > 1) {
        q = a / m;
        t = m;
        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0)
        x1 += m0;

    return x1;
}

int main() {
    // Parameters of DSA
    ll p = 23;  // Large prime number
    ll q = 11;  // Prime divisor of p-1
    ll g = 4;   // Base such that g^q % p = 1

    // Private key x
    ll x = 6;  // Random integer < q

    // Public key y
    ll y = mod_exp(g, x, p);
    cout << "Public key (y): " << y << endl;

    // Message to be signed
    ll H_m = 9;  // Example hashed value of message

    // Signing process
    ll k = 3;  // Random integer 0 < k < q
    ll r = mod_exp(g, k, p) % q;
    ll k_inv = mod_inverse(k, q);
    ll s = (k_inv * (H_m + x * r)) % q;

    cout << "Signature (r, s): (" << r << ", " << s << ")" << endl;

    // Verification process
    ll w = mod_inverse(s, q);
    ll u1 = (H_m * w) % q;
    ll u2 = (r * w) % q;
    ll v = ((mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p) % q;

    cout << "Verification result (v): " << v << endl;

    if (v == r)
        cout << "Signature is valid." << endl;
    else
        cout << "Signature is invalid." << endl;

    return 0;
}
