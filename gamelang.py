__author__ = 'WilsonKoder'

import pygame
import pygame.mixer
import sys

fileName = sys.argv[1]
pygame.mixer.init()

def game_compile(file):

    source = open(file)
    running = False
    windowName = ""
    windowSize = ""
    window = -1
    images = []
    imgID = 0
    movementVariables = []
    audioFilePath = ""

    for line in source:
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

        # elif "handle_input" in line:
        #
        #     # Usage: handle_input UP 5
        #
        #     splitted = line.split(" ")
        #     if splitted[1] == "UP":
        #         upMoveInterval = abs(int(splitted[2]))
        #         movementVariables.append([splitted[1], upMoveInterval, splitted[3].rstrip(), splitted[4].rstrip()])
        #     elif splitted[1] == "DOWN":
        #         downMoveInterval = abs(int(splitted[2]))
        #         movementVariables.append([splitted[1], downMoveInterval, splitted[3].rstrip(), splitted[4].rstrip()])
        #     elif splitted[1] == "LEFT":
        #         leftMoveInterval = abs(int(splitted[2]))
        #         movementVariables.append([splitted[1], leftMoveInterval, splitted[3].rstrip(), splitted[4].rstrip()])
        #     elif splitted[1] == "RIGHT":
        #         rightMoveInterval = abs(int(splitted[2]))
        #         movementVariables.append([splitted[1], rightMoveInterval, splitted[3].rstrip(), splitted[4].rstrip()])

        elif line == "close":
            if window != -1:
                pygame.quit()
                sys.exit()

        if "draw_image" in line:
            splitted = line.split(" ")
            path_to_image = splitted[1]
            posX = 400
            posY = 300
            exec("posX = " + splitted[2].rstrip())  # why isn't this working?
            exec("posY = " + splitted[3].rstrip())  # why isn't this working?
            print(posX)
            imgID = splitted[4].rstrip()
            pos = [int(posX), int(posY)]
            image = pygame.image.load(path_to_image)
            images.append([image, pos, imgID])

        elif "audio_play" in line:
            if window == -1:
                print("can't play music without a window")

            splitted = line.split(" ")
            filePath = splitted[1]
            audioFilePath = filePath

        elif "base_gameLoop" in line:
            splitted = line.split(" ")
            r = splitted[1]
            g = splitted[2]
            b = splitted[3]
            fillColor = (int(r), int(g), int(b))
            musicFilePath = ""
            # moveUp = False
            # moveDown = False
            # moveLeft = False
            # moveRight = False

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if musicFilePath != audioFilePath:
                    musicFilePath = audioFilePath
                    pygame.mixer.music.load(musicFilePath)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_UP or pygame.K_w:
                    #         moveUp = True
                    #     elif event.key == pygame.K_DOWN or pygame.K_s:
                    #         moveDown = True
                    #     elif event.key == pygame.K_LEFT or pygame.K_a:
                    #         moveLeft = True
                    #     elif event.key == pygame.K_RIGHT or pygame.K_d:
                    #         moveRight = True
                    #
                    # elif event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_UP or pygame.K_w:
                    #         moveUp = False
                    #     elif event.key == pygame.K_DOWN or pygame.K_s:
                    #         moveDown = False
                    #     elif event.key == pygame.K_LEFT or pygame.K_a:
                    #         moveLeft = False
                    #     elif event.key == pygame.K_RIGHT or pygame.K_d:
                    #         moveRight = False

                # if moveUp:
                #     for var in movementVariables:
                #         if var[0] == "UP":
                #             exec(var[2] + " -= " + str(var[1]))
                #             exec("print(" + var[2] + ")")
                #             for image in images:
                #                 if image[2] == var[3]:
                #                     exec("image[1][1] = " + var[2])
                #
                # elif moveDown:
                #     for var in movementVariables:
                #         if var[0] == "DOWN":
                #             exec(var[2] + " += " + str(var[1]))
                #             exec("print(" + var[2] + ")")
                #             for image in images:
                #                 if image[2] == var[3]:
                #                     exec("image[1][1] = " + var[2])
                # if moveLeft:
                #     for var in movementVariables:
                #         if var[0] == "LEFT":
                #             print(var[2])
                #             exec(var[2] + " -= " + str(var[1]))  # var[2] is variable name (xpos, ypos)
                #             exec("print(" + var[2] + ")")
                #             print(var[2])
                #             for image in images:
                #                 if image[2] == var[3]:
                #                     exec("image[1][0] = " + var[2])
                #         else:
                #             print("test")
                # elif moveRight:
                #     for var in movementVariables:
                #         if var[0] == "RIGHT":
                #             exec(var[2] + " += " + str(var[1]))
                #             exec("print(" + var[2] + ")")
                #             for image in images:
                #                 if image[2] == var[3]:
                #                     exec("image[1][0] = " + var[2])
                #         else:
                #             print("?")

                window.fill(fillColor)

                for image in images:
                    actualImage = image[0]
                    imagePos = image[1]
                    window.blit(actualImage, imagePos)

                pygame.display.flip()



game_compile(fileName)