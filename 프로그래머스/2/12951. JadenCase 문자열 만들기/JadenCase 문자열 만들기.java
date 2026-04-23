import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr = s.split(" ",-1);
        
        for (int i = 0; i < arr.length; i++){
            if (arr[i].length() == 0){
                continue;
            }
            arr[i] = arr[i].substring(0,1).toUpperCase() + arr[i].substring(1).toLowerCase();
        }
        
        answer = String.join(" ",arr);
        
        return answer;
    }
}