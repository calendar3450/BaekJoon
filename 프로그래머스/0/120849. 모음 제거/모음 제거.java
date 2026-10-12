import java.util.ArrayList;

class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        
        for (int i = 0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            
            if (c != 'a' && c != 'e' && c!='u' && c!= 'i' && c!='o') {
            answer.append(c);
            }
        }
    
        
        return answer.toString();
    }
}