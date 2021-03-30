# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    pygame.init() # 初期化
    screen = pygame.display.set_mode((800, 600)) # ウィンドウサイズの指定
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定

    while(True):
        screen.fill((0,0,0,)) # 背景色の指定。RGBだと思う
        
        #白枠を表示
        pygame.draw.lines( screen, (255, 255, 255), True, ( (200, 50), ( 600, 50), ( 600, 550), ( 200, 550)))

        pygame.display.update() # 画面更新
        
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
