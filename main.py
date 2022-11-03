'''
Meme Quiz
Author: 420s
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
game_mode = "splash"    # initialisd with splash screen

# colours to use throughout game
white = (255, 255, 255)
green = (219, 245, 208)
black = (0, 0, 0)
blue = (0, 0, 255)

# load splash screen
splash_screen_image1 = pygame.image.load("assets/images/splash.png").convert()
splash_screen_image2 = pygame.image.load("assets/images/splash2.png").convert()

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
    game_mode = "main"
    # initialise text for main menu
    mainmenu_font = pygame.font.Font('assets/ttf/roboto.ttf', 128)
    mainmenu_font2 = pygame.font.Font('assets/ttf/roboto.ttf', 64)

    mainmenu_text = mainmenu_font.render('Main Menu', True, black)
    mainmenu_start = mainmenu_font2.render('Play', True, black)
    mainmenu_options = mainmenu_font2.render('Options', True, black)
    mainmenu_quit = mainmenu_font2.render('Quit', True, black)

    mainmenu_rect = mainmenu_text.get_rect()
    mainmenu_start_rect = mainmenu_start.get_rect()
    mainmenu_options_rect = mainmenu_options.get_rect()
    mainmenu_quit_rect = mainmenu_quit.get_rect()

    mainmenu_rect.center = (380, 100)
    mainmenu_start_rect.midleft = (60, 300)
    mainmenu_options_rect.midleft = (60, 400)
    mainmenu_quit_rect.midleft = (60, 500)

    while True:
        # create blank screen
        screen.fill(green)

        # render menu options
        screen.blit(mainmenu_text, mainmenu_rect)

        screen.blit(mainmenu_start, mainmenu_start_rect)
        screen.blit(mainmenu_options, mainmenu_options_rect)
        screen.blit(mainmenu_quit, mainmenu_quit_rect)
        
        # check for player interactions
        event_list = pygame.event.get()

        for event in event_list:
            # mouse hover event
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
    quit_font = pygame.font.Font('assets/ttf/roboto.ttf', 72)
    quit_font2 = pygame.font.Font('assets/ttf/roboto.ttf', 48)

    quit_text = quit_font.render('Are you sure you want to quit?', True, black)
    quit_yes = quit_font2.render('YES', True, black)
    quit_no = quit_font2.render('NO', True, black)

    quit_text_rect = quit_text.get_rect()
    quit_no_rect = quit_no.get_rect()
    quit_yes_rect = quit_yes.get_rect()

    quit_text_rect.center = (640, 250)
    quit_yes_rect.center = (320, 340)
    quit_no_rect.center = (960, 340)


    while True:
        # create blank screen
        screen.fill(green)

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
splash_screen() # runs only once
game_mode = "main"

while True: # the main app loop

    # main menu loop
    if game_mode == "main":
        game_mode = mainmenu()
    
    # options menu loop
    if game_mode == "options":
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
    
    if game_mode == "surequit":
        game_mode = surequit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    pygame.display.update()
    clock.tick(FPS)