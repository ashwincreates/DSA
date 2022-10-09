#include<iostream>
#include<vector>
using namespace std;
int n, m;
vector<string> building;
vector<vector<bool>> visited;

void explore(int i, int j) {
    if (i == n || j == m || i < 0 || j < 0 || building[i][j] == '#' || visited[i][j])
        return;
    visited[i][j] = true;
    explore(i + 1, j);
    explore(i - 1, j);
    explore(i, j + 1);
    explore(i, j - 1);
}

int main() {
    cin >> n >> m;
    building.resize(n);
    visited.resize(n, vector<bool>(m, false));
    for (string &i: building)
        cin >> i;
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j] && building[i][j] != '#') {
                explore(i, j);
                count++;
            }
        }
    }
    cout << count;
}