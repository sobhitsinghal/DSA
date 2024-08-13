#include<bits/stdc++.h>
using namespace std;
/*
Take the day no and print the corresponding day
for 1 print Monday,
for 2 print Tuesday and so on for 7print Sunday.
*/
int main() {
    int day;
    cin >> day;

    switch(day) {
        case 1:
        cout << "Monday";
        case 2:
        cout << "Tuesday";
        case 3:
        cout << "Wednesday";
        case 4:
        cout << "Thursday";
        case 5:
        cout << "Friday";
        case 6:
        cout << "Saturday";
        case 7:
        cout << "Sunday";
        break;
        default:
        cout << "Invalid";
    }
    cout << "Check";
    return 0;
}


