n = int(input())
find_number=int(input())
board=[[0]*n for _ in range(n)]
x,y=0,0
direction=0 #처음에 아래로 이동하니깐
dxy=[[1,0],[0,1],[-1,0],[0,-1]]#아래,오른,위,왼
for i in range(n*n,0,-1):
    if i == find_number:    #찾고자 하는 값 좌표 출력
        find_x, find_y= x+1, y+1

    board[x][y] = i
    dx, dy=dxy[direction]
    nx, ny = x + dx, y + dy

    # 1. 정상 범위
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0: #인덱스 범위안이거나 초기 숫자일때
        x, y = nx, ny

    # 2.  인덱스를 벗어나거나, 다른 숫자 있음
    else: #조정이 필요, 방향전환
        direction = (direction + 1) % 4
        dx, dy=dxy[direction]
        nx, ny = x + dx, y + dy
        x, y = nx, ny
    
# 전체 표 출력
for line in board:
    for number in line:
        print(number,end=" ")
    print()
# 찾는 숫자의 좌표 출력
print(find_x, find_y)