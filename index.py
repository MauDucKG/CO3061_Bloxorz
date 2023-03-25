#!/usr/bin/python

import sys
import pygame
from ultis import *
from dfs import dfs
from bfs import bfs
from mcts import *
from astar import AStarNode, AStarSearch

import time


def draw_map(screen, node: Node, state: State, resolution_width, resolution_height):
    map = state.getMap(node)

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
        elif method_choice == 2:
            path = AStarSearch(level.state)
        elif method_choice == 3:
            path = monteSearch(level.state, 10)

        end = time.time()

        data = path[len(path) - 1].data

        str_level = str(levels_array.index(level) + 1)
        success = str(level.state.board[data[1]][data[0]]
                      == 4 and level.state.board[data[3]][data[2]] == 4)
        if success == "True":
            i += 1
        
        print("Level " + str_level + ": " + success +
              ": " + str(round(end - start, 4)) + "s, path length: ", len(path))
    print("So level success: " + str(i))
    print("Tong so level: " + str(len(levels_array)))
    input("Press enter to exit.")
    return


def testAStarSearch():
    levels_array = init_levels()
    lev = int(input("Nhap level can test: "))
    start = int(input("Nhap gia tri bat dau cua tham so: "))
    end = int(input("Nhap gia tri ket thuc cua tham so: "))
    step = int(input("Nhap buoc nhay cua tham so: "))
    minTime = 99999
    a, b, c = 0, 0, 0
    for i in range(start, end + 1, step):
        for j in range(start, end + 1, step):
            for k in range(start, end + 1, step):
                startTime = time.time()
                path = AStarSearch(levels_array[lev-1].state, i, j, k)
                endTime = time.time()

                data = path[len(path) - 1].data
                

                success = str(levels_array[lev-1].state.board[data[1]][data[0]]
                            == 4 and levels_array[lev-1].state.board[data[3]][data[2]] == 4)
                if success == "True" and endTime - startTime < minTime:
                    minTime = endTime - startTime
                    a, b, c = i, j, k

                print("case a = {}, b = {}, c = {}: ".format(i, j, k) + success + ": " + str(round(endTime - startTime, 4)) + "s")
                print("path length: ", len(path))

    print("====== Best case: a = {}, b = {}, c = {}: finish in {}".format(a, b, c, minTime))



def main():
    levels_array = init_levels()
    algorithm = "BFS"
    method_choice = int(input("Nhap method (BFS: 0, DFS: 1, A*: 2, MCTS: 3): "))
    is_test = int(input("Test hay xem UI?: (Test: 1, xem UI: 0): "))
    if is_test:
        test(levels_array, method_choice)  #
        return
    level_choice = int(input("Nhap level: "))
    done = False
    if method_choice == 0:
        path = bfs(levels_array[level_choice - 1].state)
        algorithm = "Breadth-First Search"
    elif method_choice == 1:
        path = dfs(levels_array[level_choice - 1].state)
        algorithm = "Depth-First Search"
    elif method_choice == 2:
        path = AStarSearch(levels_array[level_choice - 1].state)
        algorithm = "A* Search"
    elif method_choice == 3:
        path = monteSearch(levels_array[level_choice - 1].state, 10)
        algorithm = "Monte Carlo Tree Search"
            
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
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)

        text_surface = my_font.render(algorithm, False, (0, 0, 0))
        screen.blit(text_surface, (10, 0))

        text_surface = my_font.render('Solution: ' + str(len(path)) + ' steps', False, (0, 0, 0))
        screen.blit(text_surface, (10, 400))

        if i != 0:
            text_surface = my_font.render(str(path[i-1].data), False, (128, 128, 128))
            screen.blit(text_surface, (10, 450))

            text_surface = my_font.render('->', False, (0, 0, 0))
            screen.blit(text_surface, (210, 450))

        text_surface = my_font.render(str(path[i].data), False, (255, 255, 255))
        screen.blit(text_surface, (270, 450))

        if i != len(path) - 1:
            text_surface = my_font.render('->', False, (0, 0, 0))
            screen.blit(text_surface, (480, 450))

            text_surface = my_font.render(str(path[i+1].data), False, (128, 128, 128))
            screen.blit(text_surface, (540, 450))

        draw_map(screen, path[i], levels_array[level_choice - 1].state, resolution_width, resolution_height)
        pygame.display.flip()


main()
#testAStarSearch()
