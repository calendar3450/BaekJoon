class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        int last = -999;
        int leng = lines.length;

        int[] check = new int[201];
        
        for (int i = 0; i <leng; i++) {
            for (int j = lines[i][0]; j < lines[i][1]; j++) {
                int k = j+100;
                check[k]++;
                
                if(check[k] == 2){
                    answer++;
                }
            }
        }
        
        return answer;
    }
}