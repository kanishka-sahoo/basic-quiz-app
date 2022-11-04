'''
Meme Quiz
Author: 420s
Copyright 2022. All rights reserved.
'''
import pygame, sys

# initialise the game
pygame.init()

# Create the window, saving it to a variable.
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Meme Quiz")
FPS = 60
clock = pygame.time.Clock()
global game_mode
game_mode = "splash"    # initialised with splash screen
font_roboto = "assets/ttf/roboto.ttf"

# colours to use throughout game
white = (255, 255, 255)
lightgreen = (219, 245, 208)
lightred = (245, 219, 208)
lightblue = (208, 219, 245)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# load splash screen
splash_screen_image1 = pygame.image.load("assets/images/splash.png").convert()
splash_screen_image2 = pygame.image.load("assets/images/splash2.png").convert()

# global variables
global doSFX, doBGM
doSFX = True    # sound effects
doBGM = True    # background music

def splash_screen():
    '''renders splash screen, only for first boot '''
    # team intro scene
    for i in range(90):
        screen.fill(white)

        screen.blit(splash_screen_image1, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
        clock.tick(FPS)

    # project name screen
    for i in range(90):
        screen.fill(white)

        screen.blit(splash_screen_image2, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
        clock.tick(FPS)
    

def mainmenu():
    '''Show the main menu'''
    game_mode = "main"

    # load image
    mainmenu_img_right = pygame.image.load("assets/images/128x128.png").convert()

    # initialise the font for main menu text
    mainmenu_font = pygame.font.Font(font_roboto, 128)
    mainmenu_font2 = pygame.font.Font(font_roboto, 64)

    # Create sprites from text
    mainmenu_text = mainmenu_font.render('Meme Quiz', True, black)
    mainmenu_start = mainmenu_font2.render('Play', True, black)
    mainmenu_options = mainmenu_font2.render('Options', True, black)
    mainmenu_quit = mainmenu_font2.render('Quit', True, black)

    # Get collision and position rects
    mainmenu_rect = mainmenu_text.get_rect()
    mainmenu_start_rect = mainmenu_start.get_rect()
    mainmenu_options_rect = mainmenu_options.get_rect()
    mainmenu_quit_rect = mainmenu_quit.get_rect()

    # define positions for rects
    mainmenu_rect.midleft = (60, 100)
    mainmenu_start_rect.midleft = (60, 300)
    mainmenu_options_rect.midleft = (60, 400)
    mainmenu_quit_rect.midleft = (60, 500)

    while True:
        # create blank screen
        screen.fill(lightblue)

        # render menu options with text sprite and collision rects
        screen.blit(mainmenu_text, mainmenu_rect)

        screen.blit(mainmenu_start, mainmenu_start_rect)
        screen.blit(mainmenu_options, mainmenu_options_rect)
        screen.blit(mainmenu_quit, mainmenu_quit_rect)

        # add image
        screen.blit(mainmenu_img_right, (776, 216))
        
        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event, changes to different colour if mouse hovers
            if mainmenu_start_rect.collidepoint(pygame.mouse.get_pos()):
                mainmenu_start = mainmenu_font2.render('Play', True, blue) 
            elif mainmenu_options_rect.collidepoint(pygame.mouse.get_pos()):
                mainmenu_options = mainmenu_font2.render('Options', True, blue)
            elif mainmenu_quit_rect.collidepoint(pygame.mouse.get_pos()):
                mainmenu_quit = mainmenu_font2.render('Quit', True, blue)
            else:
                mainmenu_quit = mainmenu_font2.render('Quit', True, black)
                mainmenu_options = mainmenu_font2.render('Options', True, black)
                mainmenu_start = mainmenu_font2.render('Play', True, black)

            # mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainmenu_start_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "maingame"
                elif mainmenu_options_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "options"
                elif mainmenu_quit_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "surequit"

            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        if game_mode in ["maingame", "options", "surequit"]:
            return game_mode
        
        # update screen
        pygame.display.update()
        clock.tick(FPS)

def surequit():
    game_mode = "surequit"
    # initialise text for quit screen
    quit_font = pygame.font.Font(font_roboto, 84)
    quit_font2 = pygame.font.Font(font_roboto, 64)

    # render menu options with text sprite and collision rects
    quit_text = quit_font.render('Are you sure you want to quit?', True, black)
    quit_yes = quit_font2.render('YES', True, black)
    quit_no = quit_font2.render('NO', True, black)

    # Get collision and position rects
    quit_text_rect = quit_text.get_rect()
    quit_no_rect = quit_no.get_rect()
    quit_yes_rect = quit_yes.get_rect()

    # define positions for rects
    quit_text_rect.midleft = (60, 100)
    quit_yes_rect.midleft = (60, 300)
    quit_no_rect.midleft = (60, 400)


    while True:
        # create blank screen
        screen.fill(lightred)

        # render menu options
        screen.blit(quit_text, quit_text_rect)
        screen.blit(quit_yes, quit_yes_rect)
        screen.blit(quit_no, quit_no_rect)

        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event
            if quit_no_rect.collidepoint(pygame.mouse.get_pos()):
                quit_no = quit_font2.render('NO', True, blue)                
            elif quit_yes_rect.collidepoint(pygame.mouse.get_pos()):
                quit_yes = quit_font2.render('YES', True, blue)
            else:
                quit_yes = quit_font2.render('YES', True, black)
                quit_no = quit_font2.render('NO', True, black)

            # mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_no_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "main"
                elif quit_yes_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            
            # press cross button
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()

        if game_mode in ["main"]:
            return game_mode

        # update screen
        pygame.display.update()
        clock.tick(FPS)

def options_menu():
    '''Show options menu'''
    game_mode = "options"
    global doBGM
    global doSFX
    # initialise the font for main menu text
    options_font = pygame.font.Font(font_roboto, 128)
    options_font2 = pygame.font.Font(font_roboto, 64)

    # Create sprites from text
    options_text = options_font.render('Options', True, black)
    options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, black)
    options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, black)
    options_goback = options_font2.render('Back', True, black)

    # Get collision and position rects
    options_rect = options_text.get_rect()
    options_doSFX_rect = options_doSFX.get_rect()
    options_doBGM_rect = options_doBGM.get_rect()
    options_goback_rect = options_goback.get_rect()

    # define positions for rects
    options_rect.midleft = (60, 100)
    options_doSFX_rect.midleft = (60, 300)
    options_doBGM_rect.midleft = (60, 400)
    options_goback_rect.midleft = (60, 650)

    while True:
        # create blank screen
        screen.fill(lightgreen)

        # render menu options with text sprite and collision rects
        screen.blit(options_text, options_rect)

        screen.blit(options_doSFX, options_doSFX_rect)
        screen.blit(options_doBGM, options_doBGM_rect)
        screen.blit(options_goback, options_goback_rect)
        
        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event, changes to different colour if mouse hovers
            if options_doSFX_rect.collidepoint(pygame.mouse.get_pos()):
                options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, blue)
            elif options_doBGM_rect.collidepoint(pygame.mouse.get_pos()):
                options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, blue)
            elif options_goback_rect.collidepoint(pygame.mouse.get_pos()):
                options_goback = options_font2.render('Back', True, blue)
            else:
                options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, black)
                options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, black)
                options_goback = options_font2.render('Back', True, black)

            # mouse click event, check if user clicks on option
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_goback_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "main"
                elif options_doSFX_rect.collidepoint(pygame.mouse.get_pos()):
                    doSFX = not doSFX
                elif options_doBGM_rect.collidepoint(pygame.mouse.get_pos()):
                    doBGM = not doBGM

            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        if game_mode in ["main"]:
            return game_mode
        
        # update screen
        pygame.display.update()
        clock.tick(FPS)

splash_screen() # runs only once
game_mode = "main"

# This structure is used to avoid long function call stack
while True: # the main app loop

    # main menu loop
    if game_mode == "main":
        game_mode = mainmenu()
    
    # options menu loop
    if game_mode == "options":
        game_mode = options_menu()

    # ready to play screen
    if game_mode == "readyplay":
        pass
    # game screen loop
    if game_mode == "maingame":
        pass

    # pause menu loop
    if game_mode == "pause":
        pass
    
    # end of game, after 3 incorrect answers in a row
    if game_mode == "endscreen":
        pass
    
    # Are you sure you want to quit screen
    if game_mode == "surequit":
        game_mode = surequit()

    # check events for quit action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    pygame.display.update()
    clock.tick(FPS)