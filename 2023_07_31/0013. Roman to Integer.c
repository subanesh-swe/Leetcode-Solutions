//13. Roman to Integer

//https://leetcode.com/problems/roman-to-integer/

int getVal(char ch) {
    int val = 0;
    if (ch == 'I') val = 1;
    else if (ch == 'V') val = 5;
    else if (ch == 'X') val = 10;
    else if (ch == 'L') val = 50;
    else if (ch == 'C') val = 100;
    else if (ch == 'D') val = 500;
    else if (ch == 'M') val = 1000;
    return val;
}

int romanToInt(char* s) {
    int ans = 0, v1 = 0, v2 = 0, i = 0, l = strlen(s);
    while (i < l) {
        v1 = getVal(s[i]);
        if (i + 1 == l) {
            ans += v1;
            break;
        }
        v2 = getVal(s[i + 1]);
        if (v1 >= v2) {
            ans += v1;
            i += 1;
        }
        else {
            ans += (v2 - v1);
            i += 2;
        }
    }
    return ans;
}