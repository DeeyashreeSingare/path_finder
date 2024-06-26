import curses
from curses import wrapper
import time
from collections import deque

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze,scr,path):
    green = curses.color_pair(1)
    red = curses.color_pair(2)
    max_y, max_x = scr.getmaxyx() 
    
    

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                if i < max_y and j < max_x:
                    scr.addstr(i, j*2, "X", red)
            else:
                if i < max_y and j < max_x:
                    scr.addstr(i, j*2, maze[i][j], green)
           
def find_start(maze,start):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==start:
                return i,j
    return None
def findpath(maze,scr):
    start="O"
    end="X"
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    visited=set()
    start_pos=find_start(maze,start)
    q=deque()
    q.append((start_pos,[start_pos]))
    while q:
        (row,col),path=q.popleft()
        scr.clear()
        print_maze(maze, scr, path)
        time.sleep(0.1)
        scr.refresh()
       
        if maze[row][col]==end:
            return path
        for i,j in directions:
            nr=i+row
            nc=j+col
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]) and (nr,nc) not in visited and maze[nr][nc]==" ":
                visited.add((nr,nc))
                q.append(((nr,nc),path+[(nr,nc)]))
    print("NO PATH EXIST")
    return []


def main(scr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    findpath(maze,scr)
    scr.getch()
wrapper(main)


