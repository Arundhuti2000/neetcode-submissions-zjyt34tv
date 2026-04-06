class Solution:
    def backtrack(self, board,word, i, j,index,m,n):
        if index== len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        original_char = board[i][j]
        board[i][j] = '#'
        found_word = (
            self.backtrack(board, word, i + 1, j, index + 1, m, n) or
            self.backtrack(board, word, i - 1, j, index + 1, m, n) or
            self.backtrack(board, word, i, j + 1, index + 1, m, n) or
            self.backtrack(board, word, i, j - 1, index + 1, m, n)    
        )
        board[i][j] = original_char
        return found_word
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=[]
        curr=[]
        if not board or not board[0]:
            return False
        if not word:
            return True
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.backtrack(board, word, i, j, 0, m, n):
                        return True
        return False

    