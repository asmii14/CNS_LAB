#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++) {
        int num = arr[i];
        int even = 1;
        int odd = 1;
        bool has_even = false;  // To track if there are any non-zero even digits

        while (num != 0) {
            int digit = num % 10;
            if (digit != 0 && digit % 2 == 0) {
                even *= digit;
                has_even = true;
            } else if (digit % 2 == 1) {
                odd *= digit;
            }
            num /= 10;
        }

        // If no non-zero even digits, set even product to 0
        if (!has_even) {
            even = 0;
        }

        // Calculate the bonus rating
        int bonus = even - odd;
        if (bonus < 0) {
            arr[i] = 0;
        } else {
            arr[i] = bonus;
        }
    }

    // Print the bonus ratings
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
