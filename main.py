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
        
        
# ボールのクラス
class Ball(pygame.sprite.Sprite):
    # コンストラクタ（初期化メソッド）
    def __init__(self, filename, paddle, blocks, score, speed, angle_left, angle_right):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.dx = self.dy = 0       # ボールの速度
        self.paddle = paddle        # パドルへの参照
        self.blocks = blocks        # ブロックグループへの参照
        self.update = self.start    # ゲーム開始状態に更新
        self.score = score
        self.hit = 0                # 連続でブロックを壊した回数
        self.speed = speed          # ボールの初期速度
        self.angle_left = angle_left        # パドルの反射方向(左端:135度)
        self.angle_right = angle_right      # パドルの反射方向(右端:45度)