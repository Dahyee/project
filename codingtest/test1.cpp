#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> grade) {
    vector<int> answer;

    // 학생들마다 반복
    for(int i = 0; i < grade.size(); i++) {
        answer.push_back(1);  // 초기값 1등

        for(int j = 0; j < grade.size(); j++) {
            if(i == j)      continue;

            if(grade[i] < grade[j]) {
                answer[i]++;
            }
        }
    }

    return answer;
}
