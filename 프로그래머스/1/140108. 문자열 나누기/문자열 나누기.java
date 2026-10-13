class Solution {
    public int solution(String s) {
        int answer = 0;
        int same_cnt = 0;
        int other_cnt = 0;
        int n = s.length();
        char comp = '_';
        
        for (int i = 0; i<n; i++) {
            
            if(same_cnt == 0) {
                comp = s.charAt(i);
            }
            
            if(s.charAt(i)== comp) {
                same_cnt++;
            }
            
            else {
                other_cnt++;
            }
            
            if (same_cnt == other_cnt) {
                    same_cnt = 0;
                    other_cnt=0;
                    answer++;
            }
    
        }
        if(same_cnt != 0) {
            answer++;
        }
            
        
        return answer;
    }
}