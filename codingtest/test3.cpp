#include<vector>
#include<iostream>
#include<stdio.h>
using namespace std;

int solution(vector<vector<int> > location, vector<int> s, vector<int> e)
{
    int answer = -1;
    int ans = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    int x[2];
    int y[2];

    if(s[0] <= e[0]) {
        x[0] = s[0];
        x[1] = e[0];
    } else {
        x[0] = e[0];
        x[1] = s[0];
    }

    if(s[1] <= e[1]) {
        y[0] = s[1];
        y[1] = e[1];
    } else {
        y[0] = e[1];
        y[1] = s[1];
    }

    for(int i = 0; i < location.size(); i++) {
        if(x[0]<=location[i][0] && location[i][0]<=x[1]) {
            if(y[0]<=location[i][1] && location[i][1]<=y[1]) {
                ans++;
            }
        }
    }

    answer = ans;

    return answer;
}
