#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
const int INF = 1001001001;
using ll = long long;

// choose minimum
template<class T> void chmin(T& a, T b){
    if(a > b){
        a = b;
    }
}

int main() {
    int N;
    cin >> N;
    vector<ll> h(N);
    rep(i,N){
        cin >> h.at(i);
    }
    vector<ll> dp(N, INF);
    dp.at(0) = 0;

    rep2(i,1,N){
        chmin(dp[i],dp[i-1]+abs(h[i]-h[i-1]));
        if(i>1){
            chmin(dp[i],dp[i-2]+abs(h[i]-h[i-2]));
        }
    }
    cout << dp[N-1] << endl;
    return 0;
}
