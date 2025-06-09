# code for finding one of the solution of N - queens problem


def can_place(board, i, j, n):
    # check columns:
    for k in range(i):
        if board[k][j] == 1:
            return False

    # check left diag
    i2 = i - 1
    j2 = j - 1
    while i2 >= 0 and j2 >= 0:
        if board[i2][j2] == 1:
            return False
        i2 -= 1
        j2 -= 1

    # check right diag
    i3 = i - 1
    j3 = j + 1
    while i3 >= 0 and j3 < n:
        if board[i3][j3] == 1:
            return False
        i3 -= 1
        j3 += 1

    return True


def queen_solve(board, n, i):
    if i == n:
        # print the board
        # print(board)

        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")

            print("\n")

        # 1 way found
        return 1

    # for current row 'i' check each column position 'j'.
    ways = 0
    for j in range(n):
        if can_place(board, i, j, n):
            board[i][j] = 1

            # adding all the ways we got from each sub path
            ways += queen_solve(board, n, i + 1)

            # backtrack - remove the placed queen because later placements for queens is not possible with this queen being placed here.
            board[i][j] = 0

    return ways


n = 8
board = [[0] * n for _ in range(n)]

print(queen_solve(board, n, 0))
