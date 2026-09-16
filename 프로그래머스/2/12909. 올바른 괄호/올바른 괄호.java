class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        int count = 0;
        
        for (char word : s.toCharArray()) {
            if (word == '(') {
                count++;
            }
            else if (word==')') {
                count--;
                if (count <0) {
                    return false;
                }
            }
        }

        return count == 0;
    }
}