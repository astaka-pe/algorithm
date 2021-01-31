#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
const int INF = 1001001001;
using ll = long long;

int main(){
    int N,K;
    cin >> N >> K;
    vector<int> a(N);
    vector<int> b(N);
    rep(i,N) cin >> a.at(i);
    rep(i,N) cin >> b.at(i);
    sort(b.begin(), b.end());
    b.push_back(INF)
    int min_value = INF;
    rep(i,N){
        auto iter = lower_bound(b.begin(), b.end(), K-a.at(i));
        cout << iter << endl;
        if(a.at(i)+val < min_value){
            min_value = a.at(i) + val;
        }
    }
    cout << min_value << endl;
    return 0;
}