# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import numpy as np
import math

#定数を定義
RADIUS = 10
FRAME_LOWER = 550
FRAME_UPPER = 50
FRAME_LEFT = 200
FRAME_RIGHT = 600
FPS = 100
TIME_WAIT = 1000//FPS
INI_POSE = [400 , 200]
ROWS = 4
COLUMNS = 5
BLOCK_WIDTH = 36
BLOCK_HEIGHT = 24
X_GAP = (FRAME_RIGHT - FRAME_LEFT - (BLOCK_WIDTH * ROWS)) // (ROWS + 1)
Y_GAP = 5


def x_collision_detection( x, pre_x):
    if x + RADIUS >= FRAME_RIGHT or x - RADIUS <= FRAME_LEFT:
        if pre_x + RADIUS >= FRAME_RIGHT or pre_x - RADIUS <= FRAME_LEFT:
            return 1
        else:
            return -1
    else:
        return 1

def y_collision_detection( y, pre_y):
    if y + RADIUS >= FRAME_LOWER or y - RADIUS <= FRAME_UPPER:
        if pre_y + RADIUS >= FRAME_LOWER or pre_y - RADIUS <= FRAME_UPPER:
            return 1
        else:
            return -1
    else:
        return 1

def x_block_collision_detection( x_blo, y_blo,  x, y, pre_x ):
    points = np.array([[x_blo, y_blo], \
                       [x_blo + BLOCK_WIDTH, y_blo], \
                       [x_blo + BLOCK_WIDTH, y_blo + BLOCK_HEIGHT], \
                       [x_blo, y_blo, BLOCK_HEIGHT]])
    if points[0][1] <= y and y <= points[2][1]:
        if points[0][0] <= x + RADIUS and x + RADIUS <= points[1][0]:
            if points[0][0] <= pre_x + RADIUS and pre_x + RADIUS <= points[1][0]:
                return 1
            else :
                return -1
        elif points[0][0] <= x - RADIUS and x - RADIUS <= points[1][0]:
            if points[0][0] <= pre_x - RADIUS and pre_x - RADIUS <= points[1][0]:
                return 1
            else:
                return -1
        else:
            return 1
    else:
        return 1


def y_block_collision_detection( x_blo, y_blo, x,  y, pre_x, pre_y ):
    points = np.array([[x_blo, y_blo], \
                       [x_blo + BLOCK_WIDTH, y_blo], \
                       [x_blo + BLOCK_WIDTH, y_blo + BLOCK_HEIGHT], \
                       [x_blo, y_blo, BLOCK_HEIGHT]])
    if points[0][0] <= x and x <= points[1][0]:
        if points[0][1] <= y + RADIUS and y + RADIUS <= points[2][1]:
            if points[0][1] <= pre_y + RADIUS and pre_y + RADIUS <= points[2][1]:
                return 1
            else :
                return -1
        elif points[0][1] <= y - RADIUS and y - RADIUS <= points[2][1]:
            if points[0][1] <= pre_y - RADIUS and pre_y - RADIUS <= points[2][1]:
                return 1
            else:
                return -1
        else:
            return 1
    if math.hypot(points[0][0] - x, points[0][1] - y) <= RADIUS \
        or math.hypot(points[1][0] - x, points[1][1] - y) <= RADIUS\
        or math.hypot(points[2][0] - x, points[2][1] - y) <= RADIUS\
        or math.hypot(points[3][0] - x, points[3][1] - y) <= RADIUS:
        print("tokido")
        return -1
        """
        if math.hypot(points[0][0] - pre_x, points[0][1] - pre_y) <= RADIUS \
            or math.hypot(points[1][0] - pre_x, points[1][1] - pre_y) <= RADIUS\
            or math.hypot(points[2][0] - pre_x, points[2][1] - pre_y) <= RADIUS\
            or math.hypot(points[3][0] - pre_x, points[3][1] - pre_y) <= RADIUS:
            return 1
            
        else:
            return -1
            """
    else:
        return 1
    #for i in range(4):
      #  if math.hypot(points[i][0] - x, points[i][1] - y) <= RADIUS
       #     if math.hypot(points[i][0] - x, points[i][1] - y) >= RADIUS
def main():
    pygame.init() # 初期化
    screen = pygame.display.set_mode((800, 600)) # ウィンドウサイズの指定
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
    
    #変数
    x = INI_POSE[0]
    y = INI_POSE[1]
    dx = 100
    dy = 200
    invisible = np.zeros((COLUMNS, ROWS)) 
    print(invisible) 


    while(True):
        screen.fill(( 0, 0, 0)) # 背景色の指定。RGBだと思う
        
        pygame.time.wait( TIME_WAIT)

        #白枠を表示
        pygame.draw.lines( screen, (255, 255, 255), True, \
            ( (FRAME_LEFT, FRAME_UPPER), ( FRAME_RIGHT, FRAME_UPPER),\
            ( FRAME_RIGHT, FRAME_LOWER), ( FRAME_LEFT,FRAME_LOWER)))        
        
        #ボールを表示
        pygame.draw.circle(screen, ( 255, 0, 0),\
             (x, y), RADIUS)
        
        pre_x = x
        pre_y = y

        x = x + dx * TIME_WAIT // 1000 
        y = y + dy * TIME_WAIT // 1000
        
         
                
        for j in range(COLUMNS):
            for i in range(ROWS):
                x_block = FRAME_LEFT + X_GAP + i * X_GAP + i * BLOCK_WIDTH
                y_block = FRAME_UPPER + Y_GAP + j * Y_GAP + j * BLOCK_HEIGHT 
                if invisible[j][i] == 0:
                    screen.fill(( 255, 255, 255), \
                        ( x_block, y_block,\
                        BLOCK_WIDTH, BLOCK_HEIGHT))
                    x_col = x_block_collision_detection(x_block, y_block, x, y,  pre_x)
                    y_col = y_block_collision_detection(x_block,  y_block, x, y, pre_x, pre_y)
                    dx = dx * x_col
                    dy = dy * y_col
                    
                    if x_col == -1 or y_col == -1:
                        invisible[j][i] = 1 
                        screen.fill(( 0, 0, 0), \
                            ( x_block, y_block,\
                            BLOCK_WIDTH, BLOCK_HEIGHT))
        
        dx  = dx * x_collision_detection( x, pre_x)
        dy  = dy * y_collision_detection( y, pre_y)
                
        pygame.display.update() # 画面更新
        
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
