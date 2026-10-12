import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int num, int total) {
        List<Integer> answer = new ArrayList<>();
        
        if (total % num == 0) {
            int mid_value = total/num;
            answer.add(mid_value);
            
            for (int i = 1; i <(num/2)+1; i++) {
                answer.add(mid_value+i);
            }
            
            for (int i = 1; i<(num/2)+1; i++) {
                answer.add(0,mid_value-i);
            }
            
        }
        
        else {
            int mid_value = total / num;
            
            answer.add(mid_value);
            answer.add(mid_value+1);
            
            for (int i = 1; i<=(num/2)-1; i++) {
                answer.add(mid_value+1+i);
            }
            
            for (int i = 1; i<=(num/2)-1; i++) {
                answer.add(0,mid_value-i);
            }
            
        }
        int[] result = new int[answer.size()];
        
        for (int i = 0; i<answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}