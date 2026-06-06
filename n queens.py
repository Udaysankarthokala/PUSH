def solve_n_queens(n):

    board = [["." for _ in range(n)] for _ in range(n)]

    result = []

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):

        if row == n:

            temp = []

            for r in board:
                temp.append("".join(r))

            result.append(temp)

            return

        for col in range(n):

            if (col in cols or
                row - col in diag1 or
                row + col in diag2):
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)

    return result

print(solve_n_queens(4))