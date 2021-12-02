#include <iostream>
using namespace std;

int solution(int n)
{
    int answer = -1;
    int ans = 0;

    int number = 1;
    int arr[n];

    // 처음에는 모든 문을 연다
    for (int i = 0; i < n; i++) {
        arr[i] = 1;
    } 

    for (int number = 2; number <= n; number++) {
        // number의 배수의 문은 닫고, 나머지는 문을 연다.
        for (int i = (number-1); i < n; i++) {
            if((i+1)%number == 0) {
                if(arr[i] == 0)     arr[i] = 1;
                else                arr[i] = 0; 
            }
        }   
    } 

    // 열려있는 문의 개수를 센다.
    for (int i = 0; i < n; ++i) {
        ans += arr[i];      
    }
    answer = ans;

    return answer;
}
