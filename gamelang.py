__author__ = 'WilsonKoder'

import pygame
import sys

fileName = sys.argv[1]

def compile(file):

    source = open(file)
    running = False
    windowName = ""
    windowSize = ""
    window = -1

    for line in source:
        #print(line)
        if "print" in line:
            splitted = line.split(" ")
            exec("print(" + splitted[1] + ")")
        elif "is" in line:
            splitted = line.split("is")
            varName = splitted[0]
            varVal = splitted[1]
            exec(varName + " = " + varVal)
        elif "start" in line:
            pygame.init()
            splitted = line.split(" ")
            windowName = splitted[1]
            windowSize = (int(splitted[2]), int(splitted[3]))

            window = pygame.display.set_mode(windowSize)
            exec("pygame.display.set_caption(" + windowName + ")")

            running = True
        elif line == "close":
            if window != -1:
                pygame.quit()
            sys.exit()
        elif "base_gameLoop" in line:
            splitted = line.split(" ")
            r = splitted[1]
            g = splitted[2]
            b = splitted[3]
            fillColor = (int(r), int(g), int(b))


            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                window.fill(fillColor)
                pygame.display.flip()

compile(fileName)