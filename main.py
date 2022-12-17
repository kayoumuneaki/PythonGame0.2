# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer

# 画面サイズ
SCREEN = Rect(0, 0, 400, 400)

# パドルのクラス
class Paddle(pygame.sprite.Sprite):
    # コンストラクタ（初期化メソッド）
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20           # パドルのy座標
    
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]   # マウスのx座標をパドルのx座標に
        self.rect.clamp_ip(SCREEN)                      # ゲーム画面内のみで移動可能