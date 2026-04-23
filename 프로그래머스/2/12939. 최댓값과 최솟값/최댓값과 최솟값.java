import java.util.*;

class Solution {
    public String solution(String s) {
        String[] parts = s.split(" ");
        
        int[] arr = new int[parts.length];
        
        for(int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i]);
        }
        
        Arrays.sort(arr);
            
        int min = arr[0];
        int max = arr[arr.length-1];
            
        String answer = min + " " + max;
        
        return answer;
    }
}