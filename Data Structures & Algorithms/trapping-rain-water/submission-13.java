class Solution {
    public int trap(int[] height) {
        int p1 = 0;
        int p2 = height.length - 1;

        int right_max = height[p2];
        int left_max = height[p1];

        int answer = 0;

        while(p1 < p2){
            if(height[p1] > height[p2]){
                p2--;

                if(height[p2] > right_max){
                    right_max = height[p2];
                }
                int water = Math.min(left_max,right_max) - height[p2];
                if(water > 0){
                    answer += water;
                }
                
            }
            else{
                p1++;

                if(height[p1] > left_max){
                    left_max = height[p1];
                }
                
                int water = Math.min(left_max,right_max) - height[p1];
                if(water > 0){
                    answer += water;
                }
            
            }
        }

        return answer;
        
    }
}
