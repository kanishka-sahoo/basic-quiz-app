'''
Quiz
Author: 420s
Copyright 2022. All rights reserved.
'''
import pygame, sys

# initialise the game
pygame.init()

# Create the window, saving it to a variable.
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Quiz")
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

# load icons
arrow_img = pygame.image.load("assets/icons/arrow-left.png").convert_alpha()
cross_img = pygame.image.load("assets/icons/cross.png").convert_alpha()
qmark_img = pygame.image.load("assets/icons/qmark.png").convert_alpha()
tick_img = pygame.image.load("assets/icons/tick.png").convert_alpha()

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

def mainmenu():
    '''Show the main menu'''
    game_mode = "main"

    # load image
    mainmenu_img_right = pygame.image.load("assets/images/128x128.png").convert()

    # initialise the font for main menu text
    mainmenu_font = pygame.font.Font(font_roboto, 128)
    mainmenu_font2 = pygame.font.Font(font_roboto, 64)

    # Create sprites from text
    mainmenu_text = mainmenu_font.render('Quiz', True, black)
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
                    game_mode = "readyplay"
                elif mainmenu_options_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "options"
                elif mainmenu_quit_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "surequit"

            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        if game_mode in ["readyplay", "options", "surequit"]:
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
    quit_yes = quit_font2.render('Yes', True, black)
    quit_no = quit_font2.render('No', True, black)

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
                quit_no = quit_font2.render('No', True, blue)                
            elif quit_yes_rect.collidepoint(pygame.mouse.get_pos()):
                quit_yes = quit_font2.render('Yes', True, blue)
            else:
                quit_yes = quit_font2.render('Yes', True, black)
                quit_no = quit_font2.render('No', True, black)

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
    options_exit_img = pygame.transform.scale(arrow_img, (64, 64))
    options_text = options_font.render('Options', True, black)
    options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, black)
    options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, black)

    # Get collision and position rects
    options_exit_rect = options_exit_img.get_rect()
    options_rect = options_text.get_rect()
    options_doSFX_rect = options_doSFX.get_rect()
    options_doBGM_rect = options_doBGM.get_rect()

    # define positions for rects
    options_exit_rect.midleft = (60, 650)
    options_rect.midleft = (60, 100)
    options_doSFX_rect.midleft = (60, 300)
    options_doBGM_rect.midleft = (60, 400)

    while True:
        # create blank screen
        screen.fill(lightgreen)

        # render menu options with text sprite and collision rects
        screen.blit(options_text, options_rect)
        screen.blit(options_exit_img, options_exit_rect)
        screen.blit(options_doSFX, options_doSFX_rect)
        screen.blit(options_doBGM, options_doBGM_rect)
        
        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event, changes to different colour if mouse hovers
            if options_doSFX_rect.collidepoint(pygame.mouse.get_pos()):
                options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, blue)
            elif options_doBGM_rect.collidepoint(pygame.mouse.get_pos()):
                options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, blue)
            else:
                options_doSFX = options_font2.render('Sound Effects: '+str(doSFX), True, black)
                options_doBGM = options_font2.render('Background Music: '+str(doBGM), True, black)
            
            # mouse click event, check if user clicks on option
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_exit_rect.collidepoint(pygame.mouse.get_pos()):
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

def readyplay():
    '''ready to play screen'''
    game_mode = "surequit"
    # initialise ready to play screen
    readyplay_font = pygame.font.Font(font_roboto, 84)
    readyplay_font2 = pygame.font.Font(font_roboto, 64)

    # render menu options with text sprite and collision rects
    readyplay_text = readyplay_font.render('Are you ready to play?', True, black)
    readyplay_yes = readyplay_font2.render('Yes', True, black)
    readyplay_no = readyplay_font2.render('No', True, black)

    # Get collision and position rects
    readyplay_text_rect = readyplay_text.get_rect()
    readyplay_no_rect = readyplay_no.get_rect()
    readyplay_yes_rect = readyplay_yes.get_rect()

    # define positions for rects
    readyplay_text_rect.midleft = (60, 100)
    readyplay_yes_rect.midleft = (60, 300)
    readyplay_no_rect.midleft = (60, 400)

    while True:
        # create blank screen
        screen.fill(lightred)

        # render menu options
        screen.blit(readyplay_text, readyplay_text_rect)
        screen.blit(readyplay_yes, readyplay_yes_rect)
        screen.blit(readyplay_no, readyplay_no_rect)

        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event
            if readyplay_no_rect.collidepoint(pygame.mouse.get_pos()):
                readyplay_no = readyplay_font2.render('No', True, blue)                
            elif readyplay_yes_rect.collidepoint(pygame.mouse.get_pos()):
                readyplay_yes = readyplay_font2.render('Yes', True, blue)
            else:
                readyplay_yes = readyplay_font2.render('Yes', True, black)
                readyplay_no = readyplay_font2.render('No', True, black)

            # mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if readyplay_no_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "main"
                elif readyplay_yes_rect.collidepoint(pygame.mouse.get_pos()):
                    game_mode = "maingame"
            
            # press cross button
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()

        if game_mode in ["main", "maingame"]:
            return game_mode

        # update screen
        pygame.display.update()
        clock.tick(FPS)

def maingame():
    '''Runs the main quiz'''
    game_mode = "maingame"
    maingame_font1 = pygame.font.Font(font_roboto, 84)
    maingame_font2 = pygame.font.Font(font_roboto, 48)
    maingame_font3 = pygame.font.Font(font_roboto, 16)

    # render menu options with text sprite and collision rects
    maingame_question = maingame_font2.render('Q: 1', True, black)
    maingame_timer = maingame_font2.render('60', True, black)
    maingame_score = maingame_font2.render('Score: 0', True, black)

    # Get collision and position rects
    maingame_question_rect = maingame_question.get_rect()
    maingame_timer_rect = maingame_timer.get_rect()
    maingame_score_rect = maingame_score.get_rect()

    # define positions for rects
    maingame_question_rect.midleft = (48, 32)
    maingame_timer_rect.center = (640, 32)
    maingame_score_rect.midright = (1280-48, 32)

    question_timer = 60 # in seconds
    counter = 60 # in frames
    while True:
        screen.fill(lightblue)
        event_list = pygame.event.get()
        
        screen.blit(maingame_score, maingame_score_rect)
        screen.blit(maingame_question, maingame_question_rect)
        for event in event_list:
            # mouse hover event

        
            # press cross button
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        
        if game_mode in ["main"]:
            return game_mode
        
        # update question timer
        counter -= 1
        print(counter)
        if counter == 0:
            counter = 60
            question_timer -= 1
        
        maingame_timer = maingame_font2.render(str(question_timer), True, black)
        maingame_timer_rect = maingame_timer.get_rect()
        maingame_timer_rect.center = (640, 32)
        
        screen.blit(maingame_timer, maingame_timer_rect)

        # update screen
        pygame.display.update()
        clock.tick(FPS)

def helpmenu():
    '''Show help menu during main game'''

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
        game_mode = readyplay()
    # game screen loop
    if game_mode == "maingame":
        game_mode = maingame()

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