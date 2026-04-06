class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range (9):
                num = board[i][j]
                if not num.isdigit(): 
                    continue 
                box_row = i // 3
                box_col = j // 3
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num) 
                if num in col[j]:
                    return False
                else:
                    col[j].add(num)
                if num in boxes[box_row][box_col]:
                    return False
                else:
                    boxes[box_row][box_col].add(num)
        return True