# 가로 세로 맵크기 입력 M x N 크기 (세로=N, 가로=M)
N,M=map(int, input().split())

#현재 좌표와 방향 입력 (북: 0, 동: 1, 남: 2, 서: 3)
X, Y, direction=map(int, input().split())

#방문한 칸 저장용 2차원 리스트
d=[[0] * M for _ in range(N)]
d[X][Y]=1 #현재 위치는 방문됨 

#맵 입력받기
array=[]

for i in range(N):
  array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽으로 회전시
def turn_left():
  global direction
  direction-=1
  if direction== -1:
    direction = 3

#시작 

count =1
turn_time=0

while True:
  turn_left()
  nx= X+ dx[direction]
  ny= Y+ dy[direction]

  #방문 해본적 없는 칸이고, 육지라면
  if d[nx][ny]==0 and array[nx][ny]==0: 
    d[nx][ny]=1 #방문한다.

    X= nx
    Y= ny
    count+=1
    turn_time=0
    continue

  #이미 가본 칸이거나 바다인 경우
  else:
    turn_time += 1   # 1번 더 회전

  # 모든 방향의 칸이 전부 다 방문한 칸인 경우
  if turn_time ==4: 
    nx= X - dx[direction]
    ny= Y - dy[direction]
    #뒤로 이동 가능하다면
    if array[nx][ny] ==0:
      X=nx 
      Y=ny
    #뒤가 바다로 막힌 경우
    else:
      break
    turn_time=0

print(count)
