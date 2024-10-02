
import sys
input = sys.stdin.readline

def solution(board):
    invalid = "invalid"
    valid = "valid"
    
    xCount = board.count('X')
    oCount = board.count('O')
    dotCount = board.count('.')
    checkCount = xCount + oCount
    
    if not (xCount == oCount or xCount - oCount == 1) or checkCount < 5:
        print(invalid)
        return
    board = [list(board[i:i+3]) for i in range(0, 7, 3)]
    xBingo = checkBingo(board, 'X')
    oBingo = checkBingo(board, 'O')
    
    if oBingo:
        if not xBingo and xCount == oCount:
            print(valid)
        else:
            print(invalid)
    elif xBingo:
        if not oBingo and xCount > oCount:
            print(valid)
        else:
            print(invalid)
    elif dotCount == 0:
        print(valid)
    else: print(invalid)
    
def checkBingo(board, check):
    dest = check+check+check
    if dest in [''.join(board[i]) for i in range(3)]:
        return True
    if dest in [''.join(row[i] for row in board) for i in range(3)]:
        return True
    if dest == ''.join(board[i][i] for i in range(3)):
        return True
    if dest == ''.join(board[i][2-i] for i in range(3)):
        return True
    return False
    
while True:
    board = input().rstrip()
    if board == 'end':
        break
    solution(board)