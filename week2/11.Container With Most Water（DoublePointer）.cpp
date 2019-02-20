#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n= height.size();
        int maxv=0;
        for (int i=0,j=n-1;i<j;)
        {
            maxv = max(maxv,(j-i)*min(height[i],height[j]));
            if (height[i]<height[j])
            {
               i++;
            }
            else
            {
                j--;
            }              
        }
        return maxv;
    }
};

int main()
{
	
}
