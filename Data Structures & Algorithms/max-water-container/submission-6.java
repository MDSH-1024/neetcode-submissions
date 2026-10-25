class Solution {
    public int maxArea(int[] heights) {

     int p1 = 0;
     int p2 = heights.length - 1;
     int area = 0;
     int max_area = 0;

     while(p1 < p2){
        area = (p2 - p1)*Math.min(heights[p1], heights[p2]);

        if(area > max_area){
            max_area = area;
        }

        if(heights[p1] > heights[p2]){
            p2--;
        }
        else{
            p1++;
        }

     }

     return max_area;   
        
    }
}
