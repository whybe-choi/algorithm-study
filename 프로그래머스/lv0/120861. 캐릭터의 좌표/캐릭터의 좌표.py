def solution(keyinput, board):
    x, y = 0, 0 
    max_x = (board[0] - 1) // 2  
    max_y = (board[1] - 1) // 2 

    for key in keyinput:
        if key == "up":
            y += 1
        elif key == "down":
            y -= 1
        elif key == "left":
            x -= 1
        elif key == "right":
            x += 1
        
        if x > max_x:
            x = max_x
        elif x < -max_x:
            x = -max_x
        
        if y > max_y:
            y = max_y
        elif y < -max_y:
            y = -max_y

    answer = [x, y]
    return answer