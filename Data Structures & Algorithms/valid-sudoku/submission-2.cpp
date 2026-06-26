class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int size = 9;
        for (int i = 0; i < size; i++) {
            std::unordered_set<int> row = {};
            for (int j = 0; j < size; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int elem = board[i][j] - '0';
                if (row.find(elem) == row.end()) {
                    row.insert(elem);
                } else {
                    return false;
                }
            }
        }
        for (int j = 0; j < size; j++) {
            std::unordered_set<int> column = {};
            for (int i = 0; i < size; i++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int elem = board[i][j] - '0';
                if (column.find(elem) == column.end()) {
                    column.insert(elem);
                } else {
                    return false;
                }
            }
        }

        for (int i = 0; i < size; i+=3) {
            for (int j = 0; j < size; j+=3) {
                std::unordered_set<int> square = {};
                for (int x = i; x < i + 3; x++) {
                    for (int y = j; y < j + 3; y++) {
                        if (board[x][y] == '.') {
                            continue;
                        }
                        int elem = board[x][y] - '0';
                        if (square.find(elem) == square.end()) {
                            square.insert(elem);
                        } else {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
};
