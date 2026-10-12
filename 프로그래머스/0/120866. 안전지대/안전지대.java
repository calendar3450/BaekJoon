class Solution {
    public int solution(int[][] board) {
        int n = board.length;
        boolean[][] check = new boolean[n][n];
        int answer = 0;
        
        for (int i = 0; i<n; i++) {
            for (int j = 0; j<n; j++) {
                if (board[i][j] == 1) {
                    
                    for (int dr = -1; dr <=1; dr++) {
                        for (int dc = -1; dc <=1; dc++) {
                            int ni = i + dr;
                            int nj = j + dc;
                            
                            if (ni >=0 && ni < n && nj>=0 && nj<n) {
                                check[ni][nj] = true;
                            }
                        }
                    }
                } 
            }
        }
        
        for (int i =0; i<n; i++) {
            for (int j = 0; j<n; j++) {
                if (!check[i][j]) {
                    answer++;
                }
            }
        }
        return answer;
    }
}