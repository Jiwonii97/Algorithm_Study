/*
    >> 백준 1427번 : 소트인사이트
    입력된 숫자를 한 글자씩 읽어서 해당 숫자를 정렬한뒤 다시 출력
*/ 
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//조건 : 내림차순
bool comp(int a, int b){
    return a>b;
}

int main(){
    int input; cin>>input;
    vector<int> v;
    while(input!=0){
        int tmp;
        tmp=input%10;
        v.push_back(tmp);
        input/=10;
    }

    // algorithm 라이브러리에 있는 sort 함수사용(시작, 끝, 조건)
    sort(v.begin(), v.end(), comp);

    for(int i=0;i<v.size();i++){
        cout<<v[i];
    }
}
