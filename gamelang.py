__author__ = 'WilsonKoder'

import pygame
import pygame.mixer
import sys

fileName = sys.argv[1]
pygame.mixer.init()
pygame.init()

variables = {}
game_loop = []

def game_compile(file):

    source = open(file)
    running = False
    variables["windowName"] = ""
    variables["windowSize"] = []
    def_game_loop = False
    images = []

    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    for line in source:
        # core lang functions
        if "print" in line:
            splitted = line.split(": ")
            printText = splitted[1].rstrip()
            if "\"" not in splitted[1]:
                print(str(variables[printText]).rstrip())
            else:
                print(str(printText).replace("\"", ""))
        if "is" in line:
            splitted = line.split("is")
            varName = splitted[0].rstrip().replace(" ", "")
            varVal = splitted[1].rstrip().replace(" ", "")
            variables[varName] = varVal

        # game specific functions

        elif "window" in line:
            splitted = line.split()
            windowName = splitted[1]
            windowResX = int(splitted[2])
            windowResY = int(splitted[3])
            variables["windowSize"] = [windowResX, windowResY]
            variables["window"] = pygame.display.set_mode(variables["windowSize"])
            variables["windowName"] = windowName
            running = True
            pygame.display.set_caption(variables["windowName"])
        elif "end_window" in line:
            running = False

        elif "start_loop" in line:
            if not def_game_loop:
                def_game_loop = True
        elif "end_loop" in line:
            if def_game_loop:
                def_game_loop = False
        # drawing
        elif "draw_image" in line:
            if def_game_loop:
                splitted = line.split(" ")
                PATH = splitted[1]
                xPosition = splitted[2]
                yPosition = splitted[3].rstrip()

                position = [0, 0]

                if xPosition in variables:
                    position[0] = int(variables[xPosition])
                else:
                    position[0] = 0

                if yPosition in variables:
                    position[1] = int(variables[yPosition])
                else:
                    position[1] = 0

                image = pygame.image.load(PATH)
                images.append([image, position])

        elif "input" in line:
            # usage: input up ypos 5
            splitted = line.split(" ")
            direction = splitted[1]
            moveVar = splitted[2]
            val = int(splitted[3])
            if def_game_loop:
                if direction.lower() == "up":
                    game_loop.append(["variables[" + moveVar + "] -= " + str(val), "up"])
                elif direction.lower() == "left":
                    game_loop.append(["variables[" + moveVar + "] -= " + str(val), "left"])

                elif direction.lower() == "down":
                    game_loop.append(["variables[" + moveVar + "] += " + str(val), "down"])
                elif direction.lower() == "right":
                    game_loop.append(["variables[" + moveVar + "] += " + str(val), "right"])
        if line == "loop":
            splitted = line.split(" ")
            #fill_r = int(splitted[1])
            #fill_g = int(splitted[2])
            #fill_b = int(splitted[3])

            #fill_color = (fill_r, fill_g, fill_b)
            fill_color = (0, 255, 0)
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w or pygame.K_UP:
                            moveUp = True
                        elif event.key == pygame.K_s or pygame.K_DOWN:
                            moveDown = True
                        elif event.key == pygame.K_a or pygame.K_LEFT:
                            moveLeft = True
                        elif event.key == pygame.K_d or pygame.K_RIGHT:
                            moveRight = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or pygame.K_UP:
                            moveUp = False
                        elif event.key == pygame.K_s or pygame.K_DOWN:
                            moveDown = False
                        elif event.key == pygame.K_a or pygame.K_LEFT:
                            moveLeft = False
                        elif event.key == pygame.K_d or pygame.K_RIGHT:
                            moveRight = False

                if moveUp:
                    for command in game_loop:
                        for string in command:
                            if string == "up":
                                exec(command[0])

                if moveDown:
                    for command in game_loop:
                        for string in command:
                            if string == "down":
                                exec(command[0])
                if moveLeft:
                    for command in game_loop:
                        for string in command:
                            if string == "left":
                                exec(command[0])
                if moveRight:
                    for command in game_loop:
                        for string in command:
                            if string == "right":
                                exec(command[0])

                #for command in game_loop:
                #    if "up" or "down" or "left" or "right" not in command:
                #        exec(command[0])

                variables["window"].fill(fill_color)

                for image in images:
                    variables["window"].blit(image[0], image[1])

                pygame.display.flip()
game_compile(fileName)