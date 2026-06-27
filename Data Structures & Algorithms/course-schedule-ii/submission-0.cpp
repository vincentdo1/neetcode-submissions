class Solution {
    std::vector<int> path;
    std::unordered_map<int, std::vector<int>> prereqMap;
    std::unordered_set<int> visited;
    std::unordered_set<int> cycle;
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            prereqMap.emplace(i, vector<int>{});
        }
        for (vector<int> prereq : prerequisites) {
            int courseA = prereq[0];
            int courseB = prereq[1];
            prereqMap[courseA].push_back(courseB);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return vector<int>{};
            }

        }
        return path;
    }
    bool dfs(int course) {
            if (visited.count(course)) {
                return true;
            }
            if (cycle.count(course)) {
                return false;
            }
            vector<int> prereqs = prereqMap[course];
            cycle.insert(course);
            for (int prereq : prereqs) {
                if (!dfs(prereq)) {
                    return false;
                }
            }
            cycle.erase(course);
            visited.insert(course);
            path.push_back(course);
            return true;
        }
};
