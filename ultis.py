from random import randint, choice

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 127, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

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

def map_copy(map):
    return [list(x) for x in map]

class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, xo_objects_states={}, is_splitted=False):
        if not ((data[0] < data[2]) or (data[0] == data[2] and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.xo_objects_states = dict(xo_objects_states)
        self.is_splitted = is_splitted

    def is_stand(self):
        return self.data[0] == self.data[2] and self.data[1] == self.data[3]
    
    def __eq__(self, node: object) -> bool:
        if self.data[0] == node.data[0] and self.data[1] == node.data[1] and self.data[2] == node.data[2] \
                    and self.data[3] == node.data[3]:
                if self.xo_objects_states == node.xo_objects_states:
                    return True
                
        return False

    def __str__(self) -> str:
        return "({}, {}, {}, {})".format(self.data[0], self.data[1], self.data[2], self.data[3])

class State:
    DFS = -120
    BFS = 120

    def __init__(self, start, board=LEVEL1_ARRAY, xo_objects=None, split_objects=[]):
        if xo_objects is None:
            xo_objects = []
        self.x0, self.y0, self.x1, self.y1 = start.data # maybe delete
        self.baseboard = map_copy(board)
        self.board = map_copy(board) 
        self.states = [start]
        self.xo_objects = xo_objects
        self.visited = [start]
        self.start = start
        self.split_objects = split_objects
        # adding attribute
        self.curNode = start
        
        gx, gy = 0, 0
        while gx < len(board):
            flag = False
            while gy < len(board[gx]):
                if board[gx][gy] == 4:
                    flag = True
                    break
                gy += 1
            if flag: break
            gx += 1

        self.goal = (gx, gy)

    def next_position(self, prev_node: Node = None):
        if prev_node != self.curNode:
            raise Exception("chua set position")
        prev_node = self.curNode # i just want to keep the interface, sory :(
        #print(self.x0, self.y0, self.x1, self.y1)
        rv = []
        x0, y0, x1, y1 = prev_node.data
        if not prev_node.is_splitted:
            if self.is_stand():
                rv.append(self.add_move(rv, (x0, y0 + 1, x1, y1 + 2), prev_node))
                rv.append(self.add_move(rv, (x0, y0 - 1, x0, y0 - 2), prev_node))
                rv.append(self.add_move(rv, (x0 + 1, y0, x0 + 2, y0), prev_node))
                rv.append(self.add_move(rv, (x0 - 1, y0, x0 - 2, y1), prev_node))
            elif self.x0 == self.x1:
                rv.append(self.add_move(rv, (x0 + 1, y0, x1 + 1, y1), prev_node))
                rv.append(self.add_move(rv, (x0 - 1, y0, x1 - 1, y1), prev_node))
                rv.append(self.add_move(rv, (x0, y0 - 1, x1, y1 - 2), prev_node))
                rv.append(self.add_move(rv, (x0, y0 + 2, x1, y1 + 1), prev_node))
            elif self.y0 == self.y1:
                rv.append(self.add_move(rv, (x0, y0 + 1, x1, y1 + 1), prev_node))
                rv.append(self.add_move(rv, (x0, y0 - 1, x1, y1 - 1), prev_node))
                rv.append(self.add_move(rv, (x0 - 1, y0, x1 - 2, y1), prev_node))
                rv.append(self.add_move(rv, (x0 + 2, y0, x1 + 1, y1), prev_node))
            else:
                return []
        else:
            rv.append(self.add_move(rv, (x0, y0 + 1, x1, y1), prev_node))
            rv.append(self.add_move(rv, (x0, y0 - 1, x1, y1), prev_node))
            rv.append(self.add_move(rv, (x0 + 1, y0, x1, y1), prev_node))
            rv.append(self.add_move(rv, (x0 - 1, y0, x1, y1), prev_node))

            rv.append(self.add_move(rv, (x0, y0, x1, y1 + 1), prev_node))
            rv.append(self.add_move(rv, (x0, y0, x1, y1 - 1), prev_node))
            rv.append(self.add_move(rv, (x0, y0, x1 + 1, y1), prev_node))
            rv.append(self.add_move(rv, (x0, y0, x1 - 1, y1), prev_node))
        validNode = []
        for pos in rv:
            if self.is_valid(pos):
                validNode.append(pos)
        return validNode

    def add_move(self, rv, data, prev_node: Node):
        
        xo_objects_states = dict(prev_node.xo_objects_states)
        is_splitted = prev_node.is_splitted

        #print("add move: ", data)

        if is_splitted == False and Node(data).is_stand():
            for split_object in self.split_objects:
                if data[0] == split_object.position[0] and data[1] == split_object.position[1]:
                    data = split_object.data
                    break

        if (data[0] == data[2] and abs(data[1] - data[3]) < 2) or (data[1] == data[3] and abs(data[0] - data[2]) < 2):
            is_splitted = False
        else:
            is_splitted = True

        for xo_object in self.xo_objects:
            if (data[0] == xo_object.position[0] and data[1] == xo_object.position[1]) or (
                            data[2] == xo_object.position[0] and data[3] == xo_object.position[1]):
                if (xo_object.type == XOObject.TYPE_O) or (
                                        xo_object.type == XOObject.TYPE_X and data[0] == data[2] and data[1] == data[
                                3]):
                    for m in xo_object.managed_position:
                        if m.type == ManagedPosition.BOTH:
                            if not (prev_node.data[0] == xo_object.position[0] and prev_node.data[1] == xo_object.position[1]) or (
                            prev_node.data[2] == xo_object.position[0] and prev_node.data[3] == xo_object.position[1]):
                                xo_objects_states[(m.x, m.y)] = not xo_objects_states[(m.x, m.y)]
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            xo_objects_states[(m.x, m.y)] = True
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            xo_objects_states[(m.x, m.y)] = False
        
        #print(data)
        return Node(data, prev_node, xo_objects_states, is_splitted)

    def notContain(self, node):
        for n in self.visited:
            if n.data[0] == node.data[0] and n.data[1] == node.data[1] and n.data[2] == node.data[2] \
                    and n.data[3] == node.data[3]:
                if n.xo_objects_states == node.xo_objects_states:
                    return False
        return True

    def is_valid(self, node: Node):
        height = len(self.board)
        width = len(self.board[0])
        if node.data[0] < 0 or node.data[0] >= width or node.data[1] < 0 or node.data[1] >= height \
                or node.data[2] < 0 or node.data[2] >= width or node.data[3] < 0 or node.data[3] >= height:
            #print("invalid case 1")
            return False
        if self.board[node.data[1]][node.data[0]] == 0 or self.board[node.data[3]][
            node.data[2]] == 0:
            #print("invalid case 2")
            return False
        if node.data[0] == node.data[2] and node.data[1] == node.data[3] and self.board[node.data[1]][node.data[0]] == 5:
            #print("invalid case 3")
            return False
        

        
        for p, v in node.xo_objects_states.items():
            if not v:
                
                if (p == (node.data[0], node.data[1]) or p == (node.data[2], node.data[3])):
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

    def set_player_position(self, node: Node):
        self.x0, self.y0, self.x1, self.y1 = node.data
        self.curNode = node
        
        for p, value in node.xo_objects_states.items():
            if value:
                self.board[p[1]][p[0]] = 1
            else:
                self.board[p[1]][p[0]] = 0

    # heuristic and support function
    def distance(self, p1, p2) -> int:
        if not (0 <= p1[0] < len(self.board[0])) or not (0 <= p1[1] < len(self.board)):
            return -1
        if not (0 <= p2[0] < len(self.board[0])) or not (0 <= p2[1] < len(self.board)):
            return -1
        if p1 == p2:
            return 0

        gl = self.distance((p1[0], p1[1] - 1), p2)
        gr = self.distance((p1[0], p1[1] + 1), p2)
        gu = self.distance((p1[0] + 1, p1[1]), p2)
        gd = self.distance((p1[0] - 1, p1[1]), p2)

        dis = -1
        if gl > -1:
            if dis == -1 or gl < dis: dis = gl
            
        if gr > -1:
            if dis == -1 or gr < dis: dis = gr

        if gu > -1:
            if dis == -1 or gu < dis: dis = gu

        if gd > -1:
            if dis == -1 or gd < dis: dis = gd

        return dis

    def manhattanDis(self, p1, p2) -> int:
        if not (0 <= p1[0] < len(self.board[0])) or not (0 <= p1[1] < len(self.board)):
            return -1
        if not (0 <= p2[0] < len(self.board[0])) or not (0 <= p2[1] < len(self.board)):
            return -1
        if p1 == p2:
            return 0

        return abs(p1[0] - p2[0]) + abs(p1[1] + p2[1])

    def multiSpaceDistance(self, s1, s2) -> int:
        if s1 == -1 or s2 == -1:
            return 0
        
        if s1 == s2: return 0
        elif s1[0] > 2:
            if s2[0] <= 2:
                if s2[s1[0]%3] == s1[1]:
                    return 1
                else: return 3
            elif s2[0] > 2:
                if s1[0] != s2[0]:
                    return 2
                else: 4
        else:
            if s2[0] <= 2:
                if s1[0] == s2[0] or s1[1] == s2[1]:
                    return 2
                else: return 4
            elif s2[0] > 2:
                if s1[0] == s2[1] or s1[1] == s2[1]:
                    return 1
                else: return 4

    def findSpace(self, node: Node or tuple) -> tuple:
        if type(node) == Node:
            if node.is_splitted:
                return (-1, -1)
            elif node.is_stand():
                return (node.data[0]%3, node.data[1]%3)
            elif node.data[0] == node.data[2]: # horizon 
                lx = node.data[0] if node.data[0] < node.data[2] else node.data[2]
                return (3, (lx + 2)%3)
            else: # horizon
                uy = node.data[1] if node.data[1] < node.data[3] else node.data[3]
                return (4, (uy + 2)%3)
        else:
            return (node[0]%3, node[1]%3)

    def heuri(self, node: Node, a = 1, b = 2, c = 4):

        changeMap = 0
        for val in node.xo_objects_states.values():
            if not val: changeMap += 1
        msdis = self.multiSpaceDistance(self.findSpace(node), self.findSpace(self.goal))
        dis = -1
        if node.is_splitted:
            dis1 = self.manhattanDis((node.data[0], node.data[1]), self.goal)
            dis2 = self.manhattanDis((node.data[2], node.data[3]), self.goal)
            dis = (dis1 + dis2)/2
        else: 
            dis = self.manhattanDis((node.data[0], node.data[1]), self.goal)

        return a*dis + b*msdis + c*changeMap

    

    # gen map from a node
    def getMap(self, node: Node):
        map = self.baseboard
        for p, value in node.xo_objects_states.items():
            if value:
                map[p[1]][p[0]] = 1
            else:
                map[p[1]][p[0]] = 0
        return map

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


class SplitObject:
    def __init__(self, position, data):
        self.position = position
        self.data = data


class Level:
    def __init__(self, state):
        self.state = state


def init_levels():
    levels_array = []
    for i in range(33):
        levels_array.append(None)
    # LEVEL1 SOLVER:
    state1 = State(Node((1, 1, 1, 1), None), LEVEL1_ARRAY)
    levels_array[0] = Level(state1)

    # LEVEL2 SOLVER:
    xo_objects2 = [
        XOObject(XOObject.TYPE_O, (2, 2),
                 [ManagedPosition(4, 4, ManagedPosition.BOTH), ManagedPosition(5, 4, ManagedPosition.BOTH)]),
        XOObject(XOObject.TYPE_X, (8, 1),
                 [ManagedPosition(10, 4, ManagedPosition.BOTH), ManagedPosition(11, 4, ManagedPosition.BOTH)])]
    state2 = State(
        Node((1, 4, 1, 4), None, {(4, 4): False, (5, 4): False, (10, 4): False, (11, 4): False}),
        LEVEL2_ARRAY, xo_objects2)
    levels_array[1] = Level(state2)

    # LEVEL3 SOLVER:
    state3 = State(Node((1, 3, 1, 3), None), LEVEL3_ARRAY)
    levels_array[2] = Level(state3)

    # LEVEL4 SOLVER:
    state4 = State(Node((1, 5, 1, 5), None), LEVEL4_ARRAY)
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
        Node((13, 1, 13, 1), None, {(5, 1): True, (6, 1): True, (5, 8): True, (6, 8): True}),
        LEVEL5_ARRAY, xo_objects5)
    levels_array[4] = Level(state5)

    # LEVEL6 SOLVER:
    state6 = State(Node((0, 3, 0, 3), None), LEVEL6_ARRAY)
    levels_array[5] = Level(state6)

    # LEVEL7 SOLVER
    xo_objects7 = [XOObject(XOObject.TYPE_X, (9, 4), [ManagedPosition(3, 6, ManagedPosition.BOTH)])]
    state7 = State(Node((1, 3, 1, 3), None, {(3, 6): False}), LEVEL7_ARRAY, xo_objects7)
    levels_array[6] = Level(state7)

    # LEVEL 8 SOLVER
    split_objects8 = [SplitObject((4, 4), (10, 1, 10, 7))]
    state8 = State(Node((1, 4, 1, 4), None), LEVEL8_ARRAY, None, split_objects8)
    levels_array[7] = Level(state8)

    # LEVEL 9 SOLVER
    split_objects = [SplitObject((13, 1), (2, 1, 12, 1))]
    state9 = State(Node((1, 1, 1, 1), None), LEVEL9_ARRAY, None, split_objects)
    levels_array[8] = Level(state9)

    # LEVEL10 SOLVER
    split_objects10 = [SplitObject((12, 1), (9, 1, 12, 1))]
    xo_objects10 = [XOObject(XOObject.TYPE_O, (5, 9),
                             [ManagedPosition(3, 1, ManagedPosition.BOTH),
                              ManagedPosition(4, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (11, 9), [ManagedPosition(6, 1, ManagedPosition.BOTH),
                                                        ManagedPosition(7, 1, ManagedPosition.BOTH),
                                                        ManagedPosition(12, 2, ManagedPosition.BOTH),
                                                        ManagedPosition(12, 3, ManagedPosition.BOTH)])]
    state10 = State(Node((9, 1, 9, 1), None,
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
                                                       ManagedPosition(5, 6, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(7, 3, ManagedPosition.ONLY_ENABLE)])]
    state25 = State(Node((1, 7, 1, 7), None,
                         {(4, 6): True, (5, 6): True, (7, 3): False, (8, 4): False, (9, 4): False, (13, 2): False,
                          (13, 3): False}),
                    LEVEL25_ARRAY, xo_objects25)
    levels_array[24] = Level(state25)

    # Level 11 Solver :
    xo_objects11 = [XOObject(XOObject.TYPE_O, (6, 6),
                             [ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(4, 1, ManagedPosition.ONLY_DISABLE)])]
    state11 = State(Node((0, 5, 0, 5), None, {(4, 0): True, (4, 1): True}),
                    LEVEL11_ARRAY, xo_objects11)

    levels_array[10] = Level(state11)

    # Level 12 Solver :
    xo_objects12 = [XOObject(XOObject.TYPE_X, (6, 2),
                             [ManagedPosition(12, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 0), [ManagedPosition(6, 4, ManagedPosition.BOTH)])]
    state12 = State(Node((2, 6, 2, 6), None, {(12, 2): False, (6, 4): False}),
                    LEVEL12_ARRAY, xo_objects12)

    levels_array[11] = Level(state12)

    # LEVEL13 SOLVER:
    state13 = State(Node((12, 3, 12, 3), None), LEVEL13_ARRAY)
    levels_array[12] = Level(state13)

    # LEVEL14 SOLVER:
    xo_objects14 = [XOObject(XOObject.TYPE_X, (12, 3),
                             [ManagedPosition(1, 2, ManagedPosition.BOTH),
                              ManagedPosition(2, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (13, 9),
                             [ManagedPosition(1, 3, ManagedPosition.BOTH),
                              ManagedPosition(2, 3, ManagedPosition.BOTH)])]
    state14 = State(
        Node((4, 2, 4, 2), None, {(1, 2): False, (2, 2): False, (1, 3): False, (2, 3): False}),
        LEVEL14_ARRAY, xo_objects14)
    levels_array[13] = Level(state14)

    # LEVEL15 SOLVER:
    split_objects15 = [SplitObject((7, 5), (1, 8, 13, 1))]
    xo_objects15 = [XOObject(XOObject.TYPE_X, (12, 1),
                             [ManagedPosition(2, 2, ManagedPosition.BOTH),
                              ManagedPosition(3, 2, ManagedPosition.BOTH), ManagedPosition(5, 1, ManagedPosition.BOTH),
                              ManagedPosition(6, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (8, 3),
                             [ManagedPosition(5, 1, ManagedPosition.BOTH),
                              ManagedPosition(6, 1, ManagedPosition.BOTH), ManagedPosition(10, 1, ManagedPosition.BOTH),
                              ManagedPosition(11, 1, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (11, 7), [ManagedPosition(9, 8, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(10, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (11, 9),
                             [ManagedPosition(9, 8, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(10, 8, ManagedPosition.ONLY_DISABLE)])]
    state15 = State(
        Node((1, 8, 1, 8), None,
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
                    XOObject(XOObject.TYPE_X, (6, 1),
                             [ManagedPosition(8, 1, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(9, 1, ManagedPosition.ONLY_ENABLE)])]
    state16 = State(
        Node((3, 6, 3, 6), None,
             {(3, 1): False, (4, 1): False, (8, 1): False, (9, 1): False}),
        LEVEL16_ARRAY, xo_objects16, split_objects16)
    levels_array[15] = Level(state16)

    # LEVEL17 SOLVER:
    xo_objects17 = [XOObject(XOObject.TYPE_O, (1, 8),
                             [ManagedPosition(8, 7, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 3), [ManagedPosition(6, 6, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (13, 3), [ManagedPosition(6, 6, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 6), [ManagedPosition(7, 2, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 9), [ManagedPosition(8, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(9, 1, ManagedPosition.ONLY_ENABLE)])]
    state17 = State(Node((1, 1, 1, 1), None,
                         {(8, 7): False, (6, 6): False, (7, 2): False, (9, 1): False}),
                    LEVEL17_ARRAY, xo_objects17)
    levels_array[16] = Level(state17)

    # LEVEL18 SOLVER:
    xo_objects18 = [XOObject(XOObject.TYPE_O, (7, 0),
                             [ManagedPosition(8, 3, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(9, 3, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_O, (2, 1), [
        ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE), ManagedPosition(13, 3, ManagedPosition.ONLY_DISABLE),
        ManagedPosition(1, 8, ManagedPosition.ONLY_DISABLE), ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (1, 3), [ManagedPosition(8, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 3, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (2, 5), [ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(13, 3, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(1, 8, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (8, 6), [ManagedPosition(12, 3, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(13, 3, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(1, 8, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(2, 8, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (3, 8), [ManagedPosition(5, 4, ManagedPosition.BOTH)])]
    state18 = State(Node((2, 3, 2, 3), None,
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
        Node((1, 0, 1, 0), None, {(7, 5): False, (8, 5): False, (2, 9): True, (3, 9): True}),
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
        Node((8, 2, 8, 2), None,
             {(5, 1): True, (6, 1): True, (10, 1): False, (11, 1): False, (10, 6): False, (11, 6): False}),
        LEVEL20_ARRAY, xo_objects20, split_objects20)
    levels_array[19] = Level(state20)

    # LEVEL21 SOLVER:
    xo_objects21 = [XOObject(XOObject.TYPE_X, (8, 5),
                             [ManagedPosition(3, 9, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (8, 6), [ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state21 = State(Node((1, 3, 1, 3), None, {(3, 9): False, (5, 7): False}),
                    LEVEL21_ARRAY, xo_objects21)
    levels_array[20] = Level(state21)

    # LEVEL22 SOLVER:
    xo_objects22 = [XOObject(XOObject.TYPE_O, (6, 2),
                             [ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (4, 3), [ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (2, 9), [ManagedPosition(12, 3, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (9, 9), [ManagedPosition(2, 7, ManagedPosition.BOTH)])]
    state22 = State(Node((1, 3, 1, 3), None, {(2, 7): False, (12, 3): False}),
                    LEVEL22_ARRAY, xo_objects22)
    levels_array[21] = Level(state22)

    # LEVEL23 SOLVER:
    split_objects23 = [SplitObject((13, 7), (2, 2, 13, 7))]
    xo_objects23 = [XOObject(XOObject.TYPE_X, (2, 1),
                             [ManagedPosition(4, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 1), [ManagedPosition(1, 6, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(2, 6, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(8, 9, ManagedPosition.BOTH)
                                                        ]),
                    XOObject(XOObject.TYPE_O, (14, 3), [ManagedPosition(1, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(2, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(0, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (0, 5), [ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(14, 6, ManagedPosition.ONLY_DISABLE)])]
    state23 = State(Node((4, 7, 4, 7), None,
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
                    XOObject(XOObject.TYPE_X, (0, 3), [ManagedPosition(3, 1, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (5, 7), [ManagedPosition(8, 6, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(9, 6, ManagedPosition.ONLY_ENABLE)])]
    state24 = State(Node((1, 2, 1, 2), None,
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
        Node((10, 5, 10, 5), None, {(3, 4): False, (9, 7): False, (2, 3): True, (3, 3): True}),
        LEVEL26_ARRAY,
        xo_objects26, split_objects26)
    levels_array[25] = Level(state26)

    # LEVEL27 SOLVER:
    xo_objects27 = [XOObject(XOObject.TYPE_X, (13, 3),
                             [ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 5), [ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 5), [ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)])]
    state27 = State(Node((1, 1, 1, 1), None, {(6, 9): True, (9, 9): True}),
                    LEVEL27_ARRAY, xo_objects27)
    levels_array[26] = Level(state27)

    # LEVEL28 SOLVER:
    xo_objects28 = [XOObject(XOObject.TYPE_O, (11, 7),
                             [ManagedPosition(3, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(8, 9, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)])]
    split_objects28 = [SplitObject((11, 5), (12, 9, 14, 6))]
    state28 = State(
        Node((2, 2, 2, 2), None, {(3, 0): True, (4, 0): True, (8, 9): True, (9, 9): True}),
        LEVEL28_ARRAY, xo_objects28, split_objects28)
    levels_array[27] = Level(state28)

    # LEVEL29 SOLVER:
    xo_objects29 = [XOObject(XOObject.TYPE_O, (2, 0),
                             [ManagedPosition(10, 0, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(11, 0, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(10, 6, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 0), [
                        ManagedPosition(5, 5, ManagedPosition.ONLY_ENABLE),
                        ManagedPosition(5, 6, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (0, 3), [ManagedPosition(3, 8, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(4, 8, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(10, 9, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(11, 9, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (14, 3), [ManagedPosition(3, 9, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 6), [ManagedPosition(1, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(2, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (12, 9), [ManagedPosition(3, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(10, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(11, 0, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(12, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(13, 3, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(10, 6, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)])]

    state29 = State(Node((7, 3, 7, 3), None,
                         {(1, 3): False, (2, 3): False, (10, 6): True, (11, 6): True, (10, 9): True, (11, 9): True,
                          (5, 5): False, (5, 6): False, (3, 8): False, (4, 8): False, (10, 0): False, (11, 0): False,
                          (3, 9): False, (3, 0): True, (4, 0): True, (12, 3): False, (13, 3): False}), LEVEL29_ARRAY,
                    xo_objects29)
    levels_array[28] = Level(state29)

    # LEVEL30 SOLVER:
    xo_objects30 = [XOObject(XOObject.TYPE_X, (14, 2),
                             [ManagedPosition(10, 3, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(11, 3, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(9, 6, ManagedPosition.ONLY_ENABLE),
                              ManagedPosition(12, 6, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_X, (1, 5), [
        ManagedPosition(10, 3, ManagedPosition.ONLY_ENABLE), ManagedPosition(11, 3, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 7), [ManagedPosition(14, 7, ManagedPosition.BOTH)])]
    state30 = State(Node((2, 4, 2, 4), None,
                         {(10, 3): True, (11, 3): True, (9, 6): False, (12, 6): False, (14, 7): False}), LEVEL30_ARRAY,
                    xo_objects30)
    levels_array[29] = Level(state30)

    # LEVEL31 SOLVER:
    xo_objects31 = [XOObject(XOObject.TYPE_X, (8, 1),
                             [ManagedPosition(9, 2, ManagedPosition.BOTH),
                              ManagedPosition(10, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (6, 4), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(5, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(5, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (7, 7), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(5, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(5, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(9, 7, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (2, 8), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(14, 0, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(14, 1, ManagedPosition.ONLY_ENABLE),
                                                       ManagedPosition(14, 2, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (6, 8),
                             [ManagedPosition(4, 7, ManagedPosition.BOTH),
                              ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state31 = State(Node((12, 7, 12, 7), None,
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
    state32 = State(Node((10, 6, 10, 6), None,
                         {(4, 1): True, (5, 1): True, (2, 7): False, (3, 7): False, (2, 8): False, (3, 8): False,
                          (4, 2): False, (5, 2): False}), LEVEL32_ARRAY, xo_objects32)
    levels_array[31] = Level(state32)

    # LEVEL33 SOLVER:
    xo_objects33 = [XOObject(XOObject.TYPE_O, (7, 0),
                             [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE), ManagedPosition(4, 7,ManagedPosition.ONLY_DISABLE)]),
                    XOObject( XOObject.TYPE_O, (5, 2), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O,  (8, 2), [ManagedPosition(3,7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(4,7,ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (9, 3), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                      ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (13, 3), [ManagedPosition( 3, 7,ManagedPosition.ONLY_DISABLE),
                          ManagedPosition(  4, 7,  ManagedPosition.ONLY_DISABLE)]),
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
    state33 = State(Node((1, 3, 1, 3), None,
                         {(3, 7): True, (4, 7): True, (11, 1): False}), LEVEL33_ARRAY, xo_objects33)
    levels_array[32] = Level(state33)

    return levels_array
