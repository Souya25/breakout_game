# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


#定数を定義
RADIUS = 10
FRAME_LOWER = 50
FRAME_UPPER = 550
FRAME_LEFT = 200
FRAME_RIGHT = 600
FPS = 30
TIME_WAIT = 1000//FPS
INI_POSE = [400 , 200]

def x_collision_detection( x, pre_x):
    if x + RADIUS >= FRAME_RIGHT or x - RADIUS <= FRAME_LEFT:
        if pre_x + RADIUS >= FRAME_RIGHT or pre_x - RADIUS <= FRAME_LEFT:
            return 1
        else:
            return -1
    else:
        return 1

def y_collision_detection( y, pre_y):
    if y - RADIUS <= FRAME_LOWER or y + RADIUS >= FRAME_UPPER:
        if pre_y - RADIUS <= FRAME_LOWER or pre_y + RADIUS >= FRAME_UPPER:
            return 1
        else:
            return -1
    else:
        return 1


def main():
    pygame.init() # 初期化
    screen = pygame.display.set_mode((800, 600)) # ウィンドウサイズの指定
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定

    x = INI_POSE[0]
    y = INI_POSE[1]
    dx = 100
    dy = 200
    
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
        
         
        dx  = dx * x_collision_detection( x, pre_x)
        dy  = dy * y_collision_detection( y, pre_y)
                
        
        pygame.display.update() # 画面更新
        
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
