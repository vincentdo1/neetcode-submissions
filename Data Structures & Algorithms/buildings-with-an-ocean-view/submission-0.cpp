class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int n = heights.size();
        std::vector<int> views = {n-1};
        std::vector<int> viewsReversed;
        int currMax = heights[n-1];
        for (int i = n - 2; i >= 0; i--) {
            int height = heights[i];
            int prevHeight = heights[i + 1];
            currMax = max(prevHeight, currMax);
            if (height > currMax) {
                views.push_back(i);
            }
        }
        for (int i = views.size() - 1; i >= 0; i--) {
            viewsReversed.push_back(views[i]);
        }
        return viewsReversed;
    }
};