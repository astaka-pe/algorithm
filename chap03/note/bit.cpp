#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
const int INF = 1001001001;
using ll = long long;

int main(){
    int N, W;
    cin >> N >> W;
    vector<int> a(N);
    rep(i,N){
        cin >> a.at(i);
    }
    bool exist = false;
    //bitは2^N通りの部分集合全体を動く
    rep(bit, 1<<N){
        //cout << bit << endl;
        int sum = 0;
        rep(i,N){
            if(bit & (1<<i)){
                sum += a[i];
            }
        }
        if (sum == W){
            exist = true;
        }
    }
    if(exist) cout << "Yes" << endl;
    else cout << "No" << endl;
}