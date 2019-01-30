class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int maxv = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                maxv = max(maxv,(j-i)*min(height[i],height[j]));
            }
        }
        return maxv;
    }
};
