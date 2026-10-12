class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        
        for (int i = my_string.length()-1; i >=0; i--) {
            char c = my_string.charAt(i);
            answer.append(c);
        }
        return answer.toString();
    }
}