class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) {
            return -1;
        }
        std::queue<std::pair<int, int>> q;
        std::queue<int> lengths;
        std::vector<int> search = {-1, 0, 1};
        q.push({0,0});
        lengths.push(0);
        while (!q.empty()) {
            std::pair<int, int> idx = q.front();
            int currLength = lengths.front();
            if (idx.first == n - 1 && idx.second == n - 1) {
                return currLength + 1;
            }
            if (idx.first < 0 || idx.first >= n || idx.second < 0 || idx.second >= n || 
                grid[idx.first][idx.second] == 1) {
                q.pop();
                lengths.pop();
            } else {
                for (int i : search) {
                    for (int j : search) {
                        if (i == 0 && j == 0) {
                            continue;
                        } else {
                            q.push({idx.first + i, idx.second + j});
                            lengths.push(currLength + 1);
                        }
                    }
                }
                grid[idx.first][idx.second] = 1;
                q.pop();
                lengths.pop();
            }
        }
        return -1;        
    }

};