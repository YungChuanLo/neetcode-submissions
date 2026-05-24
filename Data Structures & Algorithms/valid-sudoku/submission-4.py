class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                block_index = 3 * (row_index // 3) + (col_index // 3)
                #move to the next value if it's empty
                if(value == "."):
                    continue
                #check if there's a duplicate in row, col, and block
                if (value in rows[row_index] or value in cols[col_index] or value in blocks[block_index]):
                    return False
                # add it to the corresponding row, col, and block
                rows[row_index].add(value)
                cols[col_index].add(value)
                # if row_index and col index < 3, 1
                #if row_index < 3 and 3<col index <6, 2
                #
                
                print(f"row index: {row_index} \n col index{col_index} \n block index{block_index}")
                blocks[block_index].add(value)
            
        return True


        