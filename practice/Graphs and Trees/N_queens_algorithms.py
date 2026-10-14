def dfs_n_queens(n):
    if n < 1:
        return []

    results = []

    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def dfs(row, current_board):
        if row == n:
            results.append(list(current_board))
            return

        for col in range(n):
            if is_valid(current_board, row, col):
                current_board.append(col)    # Place queen
                dfs(row + 1, current_board)  # Move to the next row
                current_board.pop()          # Backtrack and remove queen

    dfs(0, [])
    return results