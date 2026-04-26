import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<String> stack = new ArrayDeque<>();
        
        for (int i = 0; i < s.length(); i++){
            String text = s.substring(i,i+1);
            
            if (text.equals("(")){
                stack.push(text);
            }
            else{
                if (stack.isEmpty()){
                    return false;
                }
                stack.pop();
            }
        }
        
        if (!stack.isEmpty()){
            answer = false;
        }
        

        return answer;
    }
}