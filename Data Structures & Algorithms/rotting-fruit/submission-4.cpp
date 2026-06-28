class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int time = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    rotFruit(grid, i + 1, j, n, m, 3);
                    rotFruit(grid, i - 1, j, n, m, 3);
                    rotFruit(grid, i, j + 1, n, m, 3);
                    rotFruit(grid, i, j - 1, n, m, 3);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                std::cout<<grid[i][j]<<std::endl;
                if (grid[i][j] == 1) {
                    return -1;
                }
                time = max(time, grid[i][j]);
            }
        }
        if (time <= 2) {
            return 0;
        }
        return time - 2;
    }

    void rotFruit(vector<vector<int>>& grid, int i, int j, int n, int m, int time) {
        if (i < 0 || i >= n || j < 0 || j >= m) {
            return;
        }
        if (grid[i][j] == 0 || grid[i][j] == 2) {
            return;
        }
        
        // Already reached earlier or at the same time
        if (grid[i][j] >= 3 && grid[i][j] <= time) {
            return;
        }

        grid[i][j] = time;

        rotFruit(grid, i + 1, j, n, m, time + 1);
        rotFruit(grid, i - 1, j, n, m, time + 1);
        rotFruit(grid, i, j + 1, n, m, time + 1);
        rotFruit(grid, i, j - 1, n, m, time + 1);
    }
};
