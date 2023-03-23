#!/usr/bin/python

import sys
import pygame
from dfs import dfs
from bfs import bfs
from mcts import mcts

########################################################################################################################
# Map description:
# 1 is putable, 0 is abyss, 4 is goal (So far so well)
# LEVEL_ARRAY = np.array([
# [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])
# State: (x0,y0), (x1,y1)
# Horizontal object: (x, y), (x+1, y) or (x, y), (x, y+1).
# Vertical object: (x,y),(x,y)
# Goal state: isStand and map(y,x) = 4
########################################################################################################################
# State
# LEVEL_ARRAY = np.array([
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])

import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

LEVEL1_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]
LEVEL2_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 0, 0, 1, 4, 1],
    [1, 1, -2, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL3_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]
LEVEL4_ARRAY = [
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 1, 4, 1, 0, 0, 5, 5, 1, 5],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 5, 5, 5, 5]
]
LEVEL5_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -2],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

LEVEL6_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 4, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL7_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 4, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
LEVEL8_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 6, 1, 0, 0, 0, 1, 1, 1, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
]

LEVEL9_ARRAY = [
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 6, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
]

LEVEL10_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 4, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 6, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, -2, 0, 0, 1, 1, 1, 2, 1, 0]
]

LEVEL25_ARRAY = [
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, -2, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 4, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]

LEVEL11_ARRAY = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, -2, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]

LEVEL12_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

LEVEL13_ARRAY = [
    [1, 1, 1, 5, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 5, 5, 5, 1, 4, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 5, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 5, 5, 5, 5, 5, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 5, 5, 1, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
]

LEVEL14_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 4, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2]
]

LEVEL15_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 2, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, -2, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, -2, 1, 1, 0]
]

LEVEL16_ARRAY = [
    [0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [6, 1, 6, 0, 0, 2, 2, 1, 0, 0, 1, 4, 1],
    [0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 6, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
]

LEVEL17_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]
]

LEVEL18_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, -2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, -2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, -2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 1, 0],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]

LEVEL19_ARRAY = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, -2, 1, 1, 1, 1],
    [1, 4, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 0]
]

LEVEL20_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, -2, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, -2, 1, 0, 0, 6, 1, -2, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, -2, 1, 1],
    [1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]
LEVEL21_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 4, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
]

LEVEL22_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -2, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
]

LEVEL23_ARRAY = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -2, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 4, 1, 0, 0, 1, 1, -2],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [-2, 0, 0, 0, 1, 0, 0, 5, 5, 5, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 5, 5, 5, 5, 5, 1, 6, 1, 0],
    [0, 0, 0, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

LEVEL24_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 6],
    [0, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1],
    [2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 4, 1, 0],
    [0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 1, 0]
]
LEVEL26_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 1, 1, -2, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]

]

LEVEL27_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 5, 5, 5, 5, 1, 0, 0, -2, -2, 0],
    [1, 4, 1, 5, 5, 5, 5, 5, 5, 5, 0, 0, 1, 1, 1],
    [1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1],
    [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]

]

LEVEL28_ARRAY = [
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [5, 5, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [5, 5, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [5, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 6, 0, 0, 0],
    [0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, -2, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

LEVEL29_ARRAY = [
    [0, 0, -2, 1, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, -2, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 4, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, -2, 0, 0]
]

LEVEL30_ARRAY = [
    [0, 0, 0, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 4, 1, 1, 0, 0, 0, 0, 0, 5, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 1],
    [0, 2, 1, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 1],
    [5, 5, 5, 5, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [5, 5, 5, 1, 5, 1, 5, 5, 1, 5, 0, 0, 2, 1, 0],
    [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 0],
    [0, 5, 1, 5, 5, 5, 0, 0, 5, 5, 5, 5, 1, 0, 0]
]

LEVEL31_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 1, 4, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 5, 5, 5, 0, 0, -2, 1, 1, 0, 0, 0, 5, 0, 0],
    [0, 0, 5, 0, 0, 0, 1, 1, 1, 0, 0, 5, 5, 5, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, -2, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 2, 1, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

LEVEL32_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2, 1, 1],
    [0, 1, 4, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]

LEVEL33_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, -2, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, -2, 1, 1, -2, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, -2, -2, 1, 1, -2, 0],
    [0, 0, 0, 0, 0, 1, 1, -2, 1, 1, -2, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, -2, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1],
    [1, 4, 1, 1, 1, 1, -2, 1, 0, 0, 1, 1, 1, -2, 2],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]


########################################################################################################################
# Function map_copy. (Because python's deepcopy is extremely slow so I implement my own deepcopy)
########################################################################################################################
def map_copy(map):
    return [list(x) for x in map]


########################################################################################################################
# Data structure to store object's place, as well as its previous place and the action (up, down, left, right) to achieve it
# data: tuple (place)
# prev: Node (previous place)
# action: string (up, down, left, right)
# Created: SonPhan 23/04/2018
########################################################################################################################
class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, map=[], xo_objects_states={}, is_splitted=False):
        if not ((data[0] < data[2]) or ((data[0] == data[2]) and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.map = map_copy(map)
        self.xo_objects_states = dict(xo_objects_states)
        self.is_splitted = is_splitted

    def is_stand(self):
        return self.data[0] == self.data[2] and self.data[1] == self.data[3]


########################################################################################################################

class State:
    DFS = -120
    BFS = 120

    def __init__(self, start, board=LEVEL1_ARRAY, xo_objects=None, split_objects=[]):
        if xo_objects is None:
            xo_objects = []
        self.x0, self.y0, self.x1, self.y1 = start.data
        self.board = map_copy(board)
        self.states = [start]
        self.xo_objects = xo_objects
        self.visited = [start]
        self.start = start
        self.split_objects = split_objects

    # self.all_moves = self.next_position()

    ####################################################################################################################
    # Function to find all moves which can be reach from prev_node's move
    ####################################################################################################################
    def next_position(self, prev_node):
        rv = []
        if abs(self.x0 - self.x1) < 2 and abs(self.y0 - self.y1) < 2:
            if self.is_stand():
                self.add_move(rv, (self.x0, self.y0 + 1,
                              self.x1, self.y1 + 2), prev_node)
                self.add_move(rv, (self.x0, self.y0 - 1,
                              self.x0, self.y0 - 2), prev_node)
                self.add_move(rv, (self.x0 + 1, self.y0,
                              self.x0 + 2, self.y0), prev_node)
                self.add_move(rv, (self.x0 - 1, self.y0,
                              self.x0 - 2, self.y1), prev_node)
            elif self.x0 == self.x1:
                self.add_move(rv, (self.x0 + 1, self.y0,
                              self.x1 + 1, self.y1), prev_node)
                self.add_move(rv, (self.x0 - 1, self.y0,
                              self.x1 - 1, self.y1), prev_node)
                self.add_move(rv, (self.x0, self.y0 - 1,
                              self.x1, self.y1 - 2), prev_node)
                self.add_move(rv, (self.x0, self.y0 + 2,
                              self.x1, self.y1 + 1), prev_node)
            elif self.y0 == self.y1:
                self.add_move(rv, (self.x0, self.y0 + 1,
                              self.x1, self.y1 + 1), prev_node)
                self.add_move(rv, (self.x0, self.y0 - 1,
                              self.x1, self.y1 - 1), prev_node)
                self.add_move(rv, (self.x0 - 1, self.y0,
                              self.x1 - 2, self.y1), prev_node)
                self.add_move(rv, (self.x0 + 2, self.y0,
                              self.x1 + 1, self.y1), prev_node)
            else:
                return []
        else:
            self.add_move(rv, (self.x0, self.y0 + 1,
                          self.x1, self.y1), prev_node)
            self.add_move(rv, (self.x0, self.y0 - 1,
                          self.x1, self.y1), prev_node)
            self.add_move(rv, (self.x0 + 1, self.y0,
                          self.x1, self.y1), prev_node)
            self.add_move(rv, (self.x0 - 1, self.y0,
                          self.x1, self.y1), prev_node)

            self.add_move(
                rv, (self.x0, self.y0, self.x1, self.y1 + 1), prev_node)
            self.add_move(
                rv, (self.x0, self.y0, self.x1, self.y1 - 1), prev_node)
            self.add_move(
                rv, (self.x0, self.y0, self.x1 + 1, self.y1), prev_node)
            self.add_move(
                rv, (self.x0, self.y0, self.x1 - 1, self.y1), prev_node)

        return rv

    def add_move(self, rv, data, prev_node):
        xo_objects_states = dict(prev_node.xo_objects_states)
        is_splitted = prev_node.is_splitted
        if abs(data[0] - data[2]) < 2 and abs(data[1] - data[3]) < 2:
            is_splitted = False
        else:
            is_splitted = True
        for xo_object in self.xo_objects:
            if (data[0] == xo_object.position[0] and data[1] == xo_object.position[1]) or (
                    data[2] == xo_object.position[0] and data[3] == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if (xo_object.type == XOObject.TYPE_O) or (
                        xo_object.type == XOObject.TYPE_X and data[0] == data[2] and data[1] == data[
                            3]):
                        if m.type == ManagedPosition.BOTH:
                            xo_objects_states[(
                                m.x, m.y)] = not xo_objects_states[(m.x, m.y)]
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            xo_objects_states[(m.x, m.y)] = True
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            xo_objects_states[(m.x, m.y)] = False
        rv.append(Node(data, prev_node, prev_node.map,
                  xo_objects_states, is_splitted))

    ####################################################################################################################
    # Function to check if the object repeated previous move (which could lead to infinite loop)
    # Created: SonPhan 23/04/2018
    ####################################################################################################################
    def notContain(self, node):
        for n in self.visited:
            if n.data[0] == node.data[0] and n.data[1] == node.data[1] and n.data[2] == node.data[2] \
                    and n.data[3] == node.data[3]:
                if n.xo_objects_states == node.xo_objects_states:
                    return False
        return True

    ####################################################################################################################
    # Function to check valid move
    ####################################################################################################################
    # @staticmethod
    def is_valid(self, node):
        height = len(self.board)
        width = len(self.board[0])
        if node.data[0] < 0 or node.data[0] >= width or node.data[1] < 0 or node.data[1] >= height \
                or node.data[2] < 0 or node.data[2] >= width or node.data[3] < 0 or node.data[3] >= height:
            return False
        if node.map[node.data[1]][node.data[0]] == 0 or node.map[node.data[3]][
                node.data[2]] == 0:
            return False
        if node.data[0] == node.data[2] and node.data[1] == node.data[3] and node.map[node.data[1]][node.data[0]] == 5:
            return False
        return True

    def add_state(self, node, method):
        if self.notContain(node):
            self.visited.append(node)
            if method == self.BFS:
                self.states.append(node)
            else:
                self.states.insert(0, node)
            return True
        return False

    def add_valid_state(self, prev_node, method):
        list_node = self.next_position(prev_node)
        if not list_node:
            return False
        else:
            for node in list_node:
                if self.is_valid(node):
                    self.add_state(node, method)

    def is_goal(self, x, y):
        return self.board[y][x] == 4

    def is_stand(self):
        return self.x0 == self.x1 and self.y0 == self.y1

    def check_goal(self):
        return self.is_stand() and self.is_goal(self.x0, self.y0)

    def set_player_position(self, node):
        self.x0, self.y0, self.x1, self.y1 = node.data
        for xo_object in self.xo_objects:
            if (self.x0 == xo_object.position[0] and self.y0 == xo_object.position[1]) or (
                    self.x1 == xo_object.position[0] and self.y1 == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if xo_object.type == XOObject.TYPE_O or (xo_object.type == XOObject.TYPE_X and self.is_stand()):
                        if m.type == ManagedPosition.BOTH:
                            node.map[m.y][m.x] = abs(node.map[m.y][m.x] - 1)
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            node.map[m.y][m.x] = 1
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            node.map[m.y][m.x] = 0
        for split_object in self.split_objects:
            if self.is_stand() and self.x0 == split_object.position[0] and self.y0 == split_object.position[1]:
                self.x0, self.y0, self.x1, self.y1 = split_object.data
                node.data = split_object.data


class XOObject:
    TYPE_O = -1000
    TYPE_X = 1000

    def __init__(self, type, position=(0, 0), managed_position=[]):
        self.type = type
        self.position = position
        self.managed_position = managed_position


class ManagedPosition:
    ONLY_ENABLE = 123
    ONLY_DISABLE = -123
    BOTH = 12

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type


########################################################################################################################
# Function to solve by bfs
########################################################################################################################
# def bfs(state):
#     # start = time.time()
#     current_state = Node
#     # BFS operation
#     start = time.time()
#     while len(state.states) != 0:
#         # if time.time() - start > 15:
#         #     break
#         current_state = state.states.pop(0)
#         state.set_player_position(current_state)
#         if state.check_goal():
#             break
#         state.add_valid_state(current_state, State.BFS)
#     pointer = current_state
#     path = []
#     # Backtracking all the previous moves to reach this goal state
#     while pointer:
#         path.insert(0, pointer)
#         pointer = pointer.prev_node
#     # And print them out
#     # for p in path:
#     #     print(p.data)
#     return path


########################################################################################################################
# Function to solve by bfs
########################################################################################################################
# def dfs(state):
#     # start = time.time()
#     current_state = Node
#     # BFS operation
#     start = time.time()
#     while len(state.states) != 0:
#         # if time.time() - start > 15:
#         #     break
#         current_state = state.states.pop(0)
#         state.set_player_position(current_state)
#         if state.check_goal():
#             break
#         state.add_valid_state(current_state, State.DFS)
#     pointer = current_state
#     path = []
#     # Backtracking all the previous moves to reach this goal state
#     while pointer:
#         path.insert(0, pointer)
#         pointer = pointer.prev_node
#     # And print them out
#     # for p in path:
#     #     print(p.action)
#     return path


def draw_map(screen, node, resolution_width, resolution_height):
    map = node.map
    rect_size = 0
    if resolution_width < resolution_height:
        rect_size = int(resolution_width / 15)
    else:
        rect_size = int(resolution_height / 15)
    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    b_w = 160
    color = WHITE
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[1] and j == node.data[0]) or (i == node.data[3] and j == node.data[2]):
                b_w /= 2

    if not ((node.data[0] < node.data[2]) or ((node.data[0] == node.data[2]) and node.data[1] > node.data[3])):
            temp_data = (node.data[2], node.data[3], node.data[0], node.data[1])
            node.data = temp_data

    for i in range(len(map)):
        for j in range(len(map[i])):
            color = (199, 208, 207)
            if map[i][j] == 1:
                color = (199, 208, 207)
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang, y+h), (x+ang, y+h+10))

                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

                # pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
                # pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == -2:
                color = RED
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang, y+h), (x+ang, y+h+10))

                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

                # pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
                # pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == 2:
                color = RED
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang, y+h), (x+ang, y+h+10))

                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

                # pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
                # pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == 5:
                color = YELLOW
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang, y+h), (x+ang, y+h+10))

                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

                # pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
                # pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == 6:
                color = BLACK
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                    (x+ang, y+h), (x+ang, y+h+10))

                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

                # pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
                # pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1
    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[3] and j == node.data[2]):
                w, h = 40, 30
                ang = 15
                # b_w = 40
                # pygame.draw.polygon(screen,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)])
                # pygame.draw.polygon(screen,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1)

                # pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x-10,y+10))
                # pygame.draw.polygon(screen,BLUE,[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])
                # pygame.draw.polygon(screen,(0,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)],1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)], 1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)], 1)

                pygame.draw.line(screen, BLACK, (x-10, y), (x-10, y-b_w))
                pygame.draw.line(screen, BLACK, (x+ang+w, y -
                                 10+h), (x+ang+w, y-10+h-b_w))
                pygame.draw.line(screen, BLACK, (x+ang, y+h), (x+ang, y+h-b_w))

            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1
    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[1] and j == node.data[0]):
                w, h = 40, 30
                ang = 15
                # b_w = 40
                # pygame.draw.polygon(screen,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)])
                # pygame.draw.polygon(screen,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1)

                # pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
                # pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x-10,y+10))
                # pygame.draw.polygon(screen,BLUE,[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])
                # pygame.draw.polygon(screen,(0,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)],1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)], 1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)], 1)

                pygame.draw.line(screen, BLACK, (x-10, y), (x-10, y-b_w))
                pygame.draw.line(screen, BLACK, (x+ang+w, y -
                                 10+h), (x+ang+w, y-10+h-b_w))
                pygame.draw.line(screen, BLACK, (x+ang, y+h), (x+ang, y+h-b_w))
            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1
    # for i in range(len(map)):
    #     for j in range(len(map[i])):
    #         x,y,w,h = 40 * j,40 * i,40,30
    #         ang = 15
    #         pygame.draw.polygon(screen,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)])
    #         pygame.draw.polygon(screen,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1)
    #         pygame.draw.line(screen,(45,56,65),(x-10,y),(x-10,y+10))
    #         pygame.draw.line(screen,(45,56,65),(x+ang+w,y-10+h),(x+ang+w,y+h))
    #         pygame.draw.line(screen,(45,56,65),(x+ang,y+h),(x+ang,y+h+10))

    #         #pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
    #         #pygame.draw.line(screen,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

    #         pygame.draw.polygon(screen,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
    #         pygame.draw.polygon(screen,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
    #         pygame.draw.polygon(screen,(45,56,65),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)])
    #         pygame.draw.polygon(screen,(0,0,0),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)],1)
        # rect_points = [(30 + rect_size * j, 30 + rect_size * i),
        #                (30 + rect_size * (j + 1), 30 + rect_size * i),
        #                (30 + rect_size * (j + 1) + radio, 30 + rect_size * (i + 1)),
        #                (30 + rect_size * j + radio, 30 + rect_size * (i + 1))]
        # color = None
        # if (i == node.data[1] and j == node.data[0]) or (i == node.data[3] and j == node.data[2]):
        #     color = BLUE
        # elif map[i][j] == 1:
        #     color = WHITE
        # elif map[i][j] == -2:
        #     color = WHITE
        # elif map[i][j] == 2:
        #     color = WHITE
        # elif map[i][j] == 5:
        #     color = YELLOW
        # elif map[i][j] == 6:
        #     color = WHITE

        # if color is not None:
        #     pygame.draw.polygon(screen, color, rect_points, 0)
        #     pygame.draw.polygon(screen, BLACK, rect_points, 1)

        # if map[i][j] == -2:
        #     pygame.draw.circle(screen, RED,
        #                        [30 + rect_size * j + int(rect_size / 2),
        #                         30 + rect_size * i + int(rect_size / 2)],
        #                        int(rect_size / 2))
        # elif map[i][j] == 2:
        #     pygame.draw.aaline(screen, RED, rect_points[0], rect_points[2], 1)
        #     pygame.draw.aaline(screen, RED, rect_points[1], rect_points[3], 1)
        # elif map[i][j] == 6:
        #     pygame.draw.aaline(screen, BLACK, [30 + rect_size * j + int(rect_size / 2), 30 + rect_size * i],
        #                        [30 + rect_size * j + int(rect_size / 2), 30 + rect_size * i + rect_size])


class Level:
    def __init__(self, state):
        self.state = state


def init_levels():
    levels_array = []
    for i in range(33):
        levels_array.append(None)
    # LEVEL1 SOLVER:
    state1 = State(Node((1, 1, 1, 1), None, LEVEL1_ARRAY), LEVEL1_ARRAY)
    levels_array[0] = Level(state1)

    # LEVEL2 SOLVER:
    xo_objects2 = [
        XOObject(XOObject.TYPE_O, (2, 2),
                 [ManagedPosition(4, 4, ManagedPosition.BOTH), ManagedPosition(5, 4, ManagedPosition.BOTH)]),
        XOObject(XOObject.TYPE_X, (8, 1),
                 [ManagedPosition(10, 4, ManagedPosition.BOTH), ManagedPosition(11, 4, ManagedPosition.BOTH)])]
    state2 = State(
        Node((1, 4, 1, 4), None, LEVEL2_ARRAY, {
             (4, 4): False, (5, 4): False, (10, 4): False, (11, 4): False}),
        LEVEL2_ARRAY, xo_objects2)
    levels_array[1] = Level(state2)

    # LEVEL3 SOLVER:
    state3 = State(Node((1, 3, 1, 3), None, LEVEL3_ARRAY), LEVEL3_ARRAY)
    levels_array[2] = Level(state3)

    # LEVEL4 SOLVER:
    state4 = State(Node((1, 5, 1, 5), None, LEVEL4_ARRAY), LEVEL4_ARRAY)
    levels_array[3] = Level(state4)

    # Level 5 Solver :
    xo_objects5 = [XOObject(XOObject.TYPE_O, (8, 1),
                            [ManagedPosition(5, 1, ManagedPosition.BOTH), ManagedPosition(6, 1, ManagedPosition.BOTH)]),
                   XOObject(XOObject.TYPE_O, (3, 3), [ManagedPosition(5, 8, ManagedPosition.ONLY_ENABLE),
                                                      ManagedPosition(6, 8, ManagedPosition.ONLY_ENABLE)]),
                   XOObject(XOObject.TYPE_O, (6, 5), [ManagedPosition(5, 8, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(6, 8, ManagedPosition.ONLY_DISABLE)]),
                   XOObject(XOObject.TYPE_O, (14, 6), [
                       ManagedPosition(5, 8, ManagedPosition.BOTH), ManagedPosition(6, 8, ManagedPosition.BOTH)])]
    state5 = State(
        Node((13, 1, 13, 1), None, LEVEL5_ARRAY, {
             (5, 1): True, (6, 1): True, (5, 8): True, (6, 8): True}),
        LEVEL5_ARRAY, xo_objects5)
    levels_array[4] = Level(state5)

    # LEVEL6 SOLVER:
    state6 = State(Node((0, 3, 0, 3), None, LEVEL6_ARRAY), LEVEL6_ARRAY)
    levels_array[5] = Level(state6)

    # LEVEL7 SOLVER
    xo_objects7 = [XOObject(XOObject.TYPE_X, (9, 4), [
                            ManagedPosition(3, 6, ManagedPosition.BOTH)])]
    state7 = State(Node((1, 3, 1, 3), None, LEVEL7_ARRAY, {
                   (3, 6): False}), LEVEL7_ARRAY, xo_objects7)
    levels_array[6] = Level(state7)

    # LEVEL 8 SOLVER
    split_objects8 = [SplitObject((4, 4), (10, 1, 10, 7))]
    state8 = State(Node((1, 4, 1, 4), None, LEVEL8_ARRAY),
                   LEVEL8_ARRAY, None, split_objects8)
    levels_array[7] = Level(state8)

    # LEVEL 9 SOLVER
    split_objects = [SplitObject((13, 1), (2, 1, 12, 1))]
    state9 = State(Node((1, 1, 1, 1), None, LEVEL9_ARRAY),
                   LEVEL9_ARRAY, None, split_objects)
    levels_array[8] = Level(state9)

    # LEVEL10 SOLVER
    split_objects10 = [SplitObject((12, 1), (9, 1, 12, 1))]
    xo_objects10 = [XOObject(XOObject.TYPE_O, (5, 9),
                             [ManagedPosition(3, 1, ManagedPosition.BOTH),
                              ManagedPosition(4, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (11, 9), [ManagedPosition(6, 1, ManagedPosition.BOTH),
                                                        ManagedPosition(
                                                            7, 1, ManagedPosition.BOTH),
                                                        ManagedPosition(
                                                            12, 2, ManagedPosition.BOTH),
                                                        ManagedPosition(12, 3, ManagedPosition.BOTH)])]
    state10 = State(Node((9, 1, 9, 1), None, LEVEL10_ARRAY,
                         {(3, 1): False, (4, 1): False, (6, 1): False, (7, 1): False, (12, 2): False, (12, 3): False}),
                    LEVEL10_ARRAY,
                    xo_objects10, split_objects10)
    levels_array[9] = Level(state10)

    # LEVEL25 SOLVER
    xo_objects25 = [XOObject(XOObject.TYPE_O, (4, 2),
                             [ManagedPosition(8, 4, ManagedPosition.BOTH), ManagedPosition(9, 4, ManagedPosition.BOTH),
                              ManagedPosition(13, 2, ManagedPosition.BOTH),
                              ManagedPosition(13, 3, ManagedPosition.BOTH)]), XOObject(XOObject.TYPE_X, (2, 6), [
                                  ManagedPosition(8, 4, ManagedPosition.ONLY_ENABLE), ManagedPosition(9, 4, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (8, 8), [ManagedPosition(4, 6, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                        5, 6, ManagedPosition.ONLY_DISABLE),
                        ManagedPosition(7, 3, ManagedPosition.ONLY_ENABLE)])]
    state25 = State(Node((1, 7, 1, 7), None, LEVEL25_ARRAY,
                         {(4, 6): True, (5, 6): True, (7, 3): False, (8, 4): False, (9, 4): False, (13, 2): False,
                          (13, 3): False}),
                    LEVEL25_ARRAY, xo_objects25)
    levels_array[24] = Level(state25)

    # Level 11 Solver :
    xo_objects11 = [XOObject(XOObject.TYPE_O, (6, 6),
                             [ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(4, 1, ManagedPosition.ONLY_DISABLE)])]
    state11 = State(Node((0, 5, 0, 5), None, LEVEL11_ARRAY, {(4, 0): True, (4, 1): True}),
                    LEVEL11_ARRAY, xo_objects11)

    levels_array[10] = Level(state11)

    # Level 12 Solver :
    xo_objects12 = [XOObject(XOObject.TYPE_X, (6, 2),
                             [ManagedPosition(12, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 0), [ManagedPosition(6, 4, ManagedPosition.BOTH)])]
    state12 = State(Node((2, 6, 2, 6), None, LEVEL12_ARRAY, {(12, 2): False, (6, 4): False}),
                    LEVEL12_ARRAY, xo_objects12)

    levels_array[11] = Level(state12)

    # LEVEL13 SOLVER:
    state13 = State(Node((12, 3, 12, 3), None, LEVEL13_ARRAY), LEVEL13_ARRAY)
    levels_array[12] = Level(state13)

    # LEVEL14 SOLVER:
    xo_objects14 = [XOObject(XOObject.TYPE_X, (12, 3),
                             [ManagedPosition(1, 2, ManagedPosition.BOTH),
                              ManagedPosition(2, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (13, 9),
                             [ManagedPosition(1, 3, ManagedPosition.BOTH),
                              ManagedPosition(2, 3, ManagedPosition.BOTH)])]
    state14 = State(
        Node((4, 2, 4, 2), None, LEVEL14_ARRAY, {
             (1, 2): False, (2, 2): False, (1, 3): False, (2, 3): False}),
        LEVEL14_ARRAY, xo_objects14)
    levels_array[13] = Level(state14)

    # LEVEL15 SOLVER:
    split_objects15 = [SplitObject((7, 5), (1, 8, 13, 1))]
    xo_objects15 = [XOObject(XOObject.TYPE_X, (12, 1),
                             [ManagedPosition(2, 2, ManagedPosition.BOTH),
                              ManagedPosition(3, 2, ManagedPosition.BOTH), ManagedPosition(
                                  5, 1, ManagedPosition.BOTH),
                              ManagedPosition(6, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (8, 3),
                             [ManagedPosition(5, 1, ManagedPosition.BOTH),
                              ManagedPosition(6, 1, ManagedPosition.BOTH), ManagedPosition(
                                  10, 1, ManagedPosition.BOTH),
                              ManagedPosition(11, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (11, 7), [ManagedPosition(9, 8, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(10, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (11, 9),
                             [ManagedPosition(9, 8, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(10, 8, ManagedPosition.ONLY_DISABLE)])]
    state15 = State(
        Node((1, 8, 1, 8), None, LEVEL15_ARRAY,
             {(5, 1): True, (6, 1): True, (9, 8): True, (10, 8): True, (2, 2): False, (3, 2): False,
              (10, 1): False, (11, 1): False}),
        LEVEL15_ARRAY, xo_objects15, split_objects15)
    levels_array[14] = Level(state15)

    # LEVEL16 SOLVER:
    split_objects16 = [SplitObject((9, 6), (0, 1, 1, 0)), SplitObject((1, 0), (5, 1, 7, 1)),
                       SplitObject((0, 1), (1, 0, 2, 1)),
                       SplitObject((2, 1), (0, 1, 2, 1)), SplitObject((1, 2), (0, 1, 1, 2))]
    xo_objects16 = [XOObject(XOObject.TYPE_X, (5, 1),
                             [ManagedPosition(3, 1, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(4, 1, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (6, 1),
                             [ManagedPosition(8, 1, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(9, 1, ManagedPosition.ONLY_ENABLE)])]
    state16 = State(
        Node((3, 6, 3, 6), None, LEVEL16_ARRAY,
             {(3, 1): False, (4, 1): False, (8, 1): False, (9, 1): False}),
        LEVEL16_ARRAY, xo_objects16, split_objects16)
    levels_array[15] = Level(state16)

    # LEVEL17 SOLVER:
    xo_objects17 = [XOObject(XOObject.TYPE_O, (1, 8),
                             [ManagedPosition(8, 7, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 3), [
                             ManagedPosition(6, 6, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (13, 3), [
                             ManagedPosition(6, 6, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 6), [
                             ManagedPosition(7, 2, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 9), [ManagedPosition(8, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(9, 1, ManagedPosition.ONLY_ENABLE)])]
    state17 = State(Node((1, 1, 1, 1), None, LEVEL17_ARRAY,
                         {(1, 8): False, (8, 7): False, (6, 6): False, (7, 2): False, (8, 7): False, (9, 1): False}),
                    LEVEL17_ARRAY, xo_objects17)
    levels_array[16] = Level(state17)

    # LEVEL18 SOLVER:
    xo_objects18 = [XOObject(XOObject.TYPE_O, (7, 0),
                             [ManagedPosition(8, 3, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(9, 3, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_O, (2, 1), [
                                  ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE), ManagedPosition(
                                      13, 3, ManagedPosition.ONLY_DISABLE),
                                  ManagedPosition(1, 8, ManagedPosition.ONLY_DISABLE), ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (1, 3), [ManagedPosition(8, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 3, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (2, 5), [ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                        13, 3, ManagedPosition.ONLY_DISABLE),
                        ManagedPosition(
                        1, 8, ManagedPosition.ONLY_DISABLE),
                        ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (8, 6), [ManagedPosition(12, 3, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(
                        13, 3, ManagedPosition.ONLY_ENABLE),
                        ManagedPosition(
                        1, 8, ManagedPosition.ONLY_ENABLE),
                        ManagedPosition(2, 8, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (3, 8), [ManagedPosition(5, 4, ManagedPosition.BOTH)])]
    state18 = State(Node((2, 3, 2, 3), None, LEVEL18_ARRAY,
                         {(8, 3): False, (9, 3): False, (12, 3): False, (13, 3): False, (1, 8): False, (2, 8): False,
                          (5, 4): False}),
                    LEVEL18_ARRAY, xo_objects18)

    levels_array[17] = Level(state18)

    # LEVEL19 SOLVER:
    xo_objects19 = [XOObject(XOObject.TYPE_O, (10, 0),
                             [ManagedPosition(7, 5, ManagedPosition.BOTH),
                              ManagedPosition(8, 5, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (10, 5), [ManagedPosition(2, 9, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(3, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (10, 9), [ManagedPosition(2, 9, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(3, 9, ManagedPosition.ONLY_ENABLE)])]
    state19 = State(
        Node((1, 0, 1, 0), None, LEVEL19_ARRAY, {
             (7, 5): False, (8, 5): False, (2, 9): True, (3, 9): True}),
        LEVEL19_ARRAY, xo_objects19)
    levels_array[18] = Level(state19)

    # LEVEL20 SOLVER:
    split_objects20 = [SplitObject((7, 4), (13, 1, 13, 7))]
    xo_objects20 = [XOObject(XOObject.TYPE_O, (7, 2),
                             [ManagedPosition(5, 1, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(6, 1, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (3, 4),
                             [ManagedPosition(5, 1, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(6, 1, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (9, 4), [ManagedPosition(5, 1, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(6, 1, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (1, 7),
                             [ManagedPosition(10, 1, ManagedPosition.BOTH),
                              ManagedPosition(11, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (12, 6),
                             [ManagedPosition(10, 6, ManagedPosition.BOTH),
                              ManagedPosition(11, 6, ManagedPosition.BOTH)])
                    ]
    state20 = State(
        Node((8, 2, 8, 2), None, LEVEL20_ARRAY,
             {(5, 1): True, (6, 1): True, (10, 1): False, (11, 1): False, (10, 6): False, (11, 6): False}),
        LEVEL20_ARRAY, xo_objects20, split_objects20)
    levels_array[19] = Level(state20)

    # LEVEL21 SOLVER:
    xo_objects21 = [XOObject(XOObject.TYPE_X, (8, 5),
                             [ManagedPosition(3, 9, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (8, 6), [ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state21 = State(Node((1, 3, 1, 3), None, LEVEL21_ARRAY, {(3, 9): False, (5, 7): False}),
                    LEVEL21_ARRAY, xo_objects21)
    levels_array[20] = Level(state21)

    # LEVEL22 SOLVER:
    xo_objects22 = [XOObject(XOObject.TYPE_O, (6, 2),
                             [ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (4, 3), [
                             ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (2, 9), [
                             ManagedPosition(12, 3, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (9, 9), [ManagedPosition(2, 7, ManagedPosition.BOTH)])]
    state22 = State(Node((1, 3, 1, 3), None, LEVEL22_ARRAY, {(2, 7): False, (12, 3): False}),
                    LEVEL22_ARRAY, xo_objects22)
    levels_array[21] = Level(state22)

    # LEVEL23 SOLVER:
    split_objects23 = [SplitObject((13, 7), (2, 2, 13, 7))]
    xo_objects23 = [XOObject(XOObject.TYPE_X, (2, 1),
                             [ManagedPosition(4, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 1), [ManagedPosition(1, 6, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(
                                                            2, 6, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(
                                                            8, 9, ManagedPosition.BOTH)
                                                        ]),
                    XOObject(XOObject.TYPE_O, (14, 3), [ManagedPosition(1, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(
                                                            2, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(0, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (0, 5), [ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(14, 6, ManagedPosition.ONLY_DISABLE)])]
    state23 = State(Node((4, 7, 4, 7), None, LEVEL23_ARRAY,
                         {(9, 2): True, (10, 2): True, (14, 6): True, (1, 6): False, (2, 6): False, (0, 3): False,
                          (8, 9): False}),
                    LEVEL23_ARRAY, xo_objects23, split_objects23)
    levels_array[22] = Level(state23)

    # LEVEL24 SOLVER:
    split_objects24 = [SplitObject((13, 1), (5, 6, 7, 6))]
    xo_objects24 = [XOObject(XOObject.TYPE_X, (11, 1),
                             [ManagedPosition(2, 2, ManagedPosition.BOTH),
                              ManagedPosition(3, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (5, 2), [ManagedPosition(7, 7, ManagedPosition.ONLY_ENABLE)
                                                       ]),
                    XOObject(XOObject.TYPE_X, (0, 3), [
                             ManagedPosition(3, 1, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (5, 7), [ManagedPosition(8, 6, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(9, 6, ManagedPosition.ONLY_ENABLE)])]
    state24 = State(Node((1, 2, 1, 2), None, LEVEL24_ARRAY,
                         {(2, 2): False, (3, 2): False, (7, 7): False,
                          (3, 1): False, (8, 6): False, (9, 6): False}),
                    LEVEL24_ARRAY, xo_objects24, split_objects24)
    levels_array[23] = Level(state24)

    # LEVEL26 SOLVER:
    xo_objects26 = [XOObject(XOObject.TYPE_X, (1, 7), [ManagedPosition(3, 4, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(9, 7, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (7, 1), [ManagedPosition(2, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(3, 3, ManagedPosition.ONLY_DISABLE)])]
    split_objects26 = [SplitObject((13, 0), (10, 5, 12, 3))]
    state26 = State(
        Node((10, 5, 10, 5), None, LEVEL26_ARRAY, {
             (3, 4): False, (9, 7): False, (2, 3): True, (3, 3): True}),
        LEVEL26_ARRAY,
        xo_objects26, split_objects26)
    levels_array[25] = Level(state26)

    # LEVEL27 SOLVER:
    xo_objects27 = [XOObject(XOObject.TYPE_X, (13, 3),
                             [ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 5), [
                             ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 5), [ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)])]
    state27 = State(Node((1, 1, 1, 1), None, LEVEL27_ARRAY, {(6, 9): True, (9, 9): True}),
                    LEVEL27_ARRAY, xo_objects27)
    levels_array[26] = Level(state27)

    # LEVEL28 SOLVER:
    xo_objects28 = [XOObject(XOObject.TYPE_O, (11, 7),
                             [ManagedPosition(3, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(
                                  4, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(
                                  8, 9, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)])]
    split_objects28 = [SplitObject((11, 5), (12, 9, 14, 6))]
    state28 = State(
        Node((2, 2, 2, 2), None, LEVEL28_ARRAY, {
             (3, 0): True, (4, 0): True, (8, 9): True, (9, 9): True}),
        LEVEL28_ARRAY, xo_objects28, split_objects28)
    levels_array[27] = Level(state28)

    # LEVEL29 SOLVER:
    xo_objects29 = [XOObject(XOObject.TYPE_O, (2, 0),
                             [ManagedPosition(10, 0, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(
                                  11, 0, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(
                                  10, 6, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 0), [
                        ManagedPosition(5, 5, ManagedPosition.ONLY_ENABLE),
                        ManagedPosition(5, 6, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (0, 3), [ManagedPosition(3, 8, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(
                                                           4, 8, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(
                                                           10, 9, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(11, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (14, 3), [
                             ManagedPosition(3, 9, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 6), [ManagedPosition(1, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(2, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 9), [ManagedPosition(3, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(
                                                            4, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(
                                                            10, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(
                                                            11, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(
                                                            12, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(
                                                            13, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(
                                                            10, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)])]

    state29 = State(Node((7, 3, 7, 3), None, LEVEL29_ARRAY,
                         {(1, 3): False, (2, 3): False, (10, 6): True, (11, 6): True, (10, 9): True, (11, 9): True,
                          (5, 5): False, (5, 6): False, (3, 8): False, (4, 8): False, (10, 0): False, (11, 0): False,
                          (3, 9): False, (3, 0): True, (4, 0): True, (12, 3): False, (13, 3): False}), LEVEL29_ARRAY,
                    xo_objects29)
    levels_array[28] = Level(state29)

    # LEVEL30 SOLVER:
    xo_objects30 = [XOObject(XOObject.TYPE_X, (14, 2),
                             [ManagedPosition(10, 3, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(
                                  11, 3, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(
                                  9, 6, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(12, 6, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_X, (1, 5), [
                                  ManagedPosition(10, 3, ManagedPosition.ONLY_ENABLE), ManagedPosition(11, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 7), [ManagedPosition(14, 7, ManagedPosition.BOTH)])]
    state30 = State(Node((2, 4, 2, 4), None, LEVEL30_ARRAY,
                         {(10, 3): True, (11, 3): True, (9, 6): False, (12, 6): False, (14, 7): False}), LEVEL30_ARRAY,
                    xo_objects30)
    levels_array[29] = Level(state30)

    # LEVEL31 SOLVER:
    xo_objects31 = [XOObject(XOObject.TYPE_X, (8, 1),
                             [ManagedPosition(9, 2, ManagedPosition.BOTH),
                              ManagedPosition(10, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (6, 4), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           5, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           4, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           5, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           9, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (7, 7), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           5, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           4, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           5, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           9, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (2, 8), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(
                                                           14, 0, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(
                                                           14, 1, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(14, 2, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (6, 8),
                             [ManagedPosition(4, 7, ManagedPosition.BOTH),
                              ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state31 = State(Node((12, 7, 12, 7), None, LEVEL31_ARRAY,
                         {(9, 7): True, (10, 7): True, (4, 2): True, (5, 2): True, (9, 2): False, (10, 2): False,
                          (4, 7): False, (5, 7): False, (14, 0): False, (14, 1): False, (14, 2): False}), LEVEL31_ARRAY,
                    xo_objects31)
    levels_array[30] = Level(state31)

    # LEVEL32 SOLVER:
    xo_objects32 = [XOObject(XOObject.TYPE_X, (13, 0),
                             [ManagedPosition(4, 1, ManagedPosition.BOTH), ManagedPosition(5, 1, ManagedPosition.BOTH),
                              ManagedPosition(2, 7, ManagedPosition.BOTH),
                              ManagedPosition(3, 7, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (11, 2),
                             [ManagedPosition(2, 8, ManagedPosition.BOTH),
                              ManagedPosition(3, 8, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (5, 7),
                             [ManagedPosition(4, 2, ManagedPosition.BOTH),
                              ManagedPosition(5, 2, ManagedPosition.BOTH)])]
    state32 = State(Node((10, 6, 10, 6), None, LEVEL32_ARRAY,
                         {(4, 1): True, (5, 1): True, (2, 7): False, (3, 7): False, (2, 8): False, (3, 8): False,
                          (4, 2): False, (5, 2): False}), LEVEL32_ARRAY, xo_objects32)
    levels_array[31] = Level(state32)

    # LEVEL33 SOLVER:
    xo_objects33 = [XOObject(XOObject.TYPE_O, (7, 0),
                             [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE), ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (5, 2), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O,  (8, 2), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (9, 3), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 3), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(4, 7,  ManagedPosition.ONLY_DISABLE)]),
                    XOObject(
                        XOObject.TYPE_O, (7, 4), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (10, 3), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),


                    XOObject(XOObject.TYPE_O,
                             (10, 4), [
                                 ManagedPosition(3,
                                                 7,
                                                 ManagedPosition.ONLY_DISABLE),
                                 ManagedPosition(4,
                                                 7,
                                                 ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (11, 5), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                   ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_O,
                                                                                                   (11, 6), [
                                                                                                       ManagedPosition(
                                                                                                           3, 7,
                                                                                                           ManagedPosition.ONLY_DISABLE),
                                                                                                       ManagedPosition(
                                                                                                           4, 7,
                                                                                                           ManagedPosition.ONLY_DISABLE)]),
                    XOObject(
                        XOObject.TYPE_O, (13, 7), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                   ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(
                        XOObject.TYPE_O, (6, 7), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X,
                             (14, 7), [
                                 ManagedPosition(
                                     11, 1,
                                     ManagedPosition.ONLY_ENABLE)])]
    state33 = State(Node((1, 3, 1, 3), None, LEVEL33_ARRAY,
                         {(3, 7): True, (4, 7): True, (11, 1): False}), LEVEL33_ARRAY, xo_objects33)
    levels_array[32] = Level(state33)

    return levels_array


def test(levels_array, method_choice):
    ######################
    # TEST################
    i = 0
    for level in levels_array:
        if level is None:
            continue
        start = time.time()
        if method_choice == 1:
            path = dfs(level.state)
        elif method_choice == 0:
            path = bfs(level.state)
        elif method_choice == 3:
            path = mcts(level.state)
        data = path[len(path) - 1].data

        str_level = str(levels_array.index(level) + 1)
        success = str(level.state.board[data[1]][data[0]]
                      == 4 and level.state.board[data[3]][data[2]] == 4)
        if success == "True":
            i += 1
        end = time.time()
        print("Level " + str_level + ": " + success +
              ": " + str(round(end - start, 4)) + "s")
    print("So level success: " + str(i))
    print("Tong so level: " + str(len(list(filter(None.__ne__, levels_array)))))
    input("Press any key to exit.")
    return


class SplitObject:
    def __init__(self, position, data):
        self.position = position
        self.data = data


def main():
    levels_array = init_levels()
    method_choice = int(input("Nhap method (BFS: 0, DFS: 1, MCTS: 3): "))
    is_test = int(input("Test hay xem UI?: (Test: 1, xem UI: 0): "))
    if is_test:
        test(levels_array, method_choice)  #
        return
    level_choice = int(input("Nhap level: "))
    done = False
    if method_choice == 0:
        path = bfs(levels_array[level_choice - 1].state)
    elif method_choice == 1:
        path = dfs(levels_array[level_choice - 1].state)
    elif method_choice == 3:
        path = mcts(levels_array[level_choice - 1].state)
    pygame.init()
    pygame.display.set_caption("Bloxorz")

    resolution_height = pygame.display.Info().current_h / 1.5
    resolution_width = pygame.display.Info().current_w / 1.5

    screen = pygame.display.set_mode((resolution_width, resolution_height))
    i = 0
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if i < len(path) - 1:
                        i += 1
                elif event.key == pygame.K_LEFT:
                    if i > 0:
                        i -= 1
        screen.fill(GREEN)

        draw_map(screen, path[i], resolution_width, resolution_height)
        pygame.display.flip()


main()
