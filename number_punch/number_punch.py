import sys
import random
import pygame

# Define Window Size
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# Define Frames Per Second
FRAMES_PER_SEC = 25

# Function: Draw a text to the screen
def blit_text(screen_object, font, msg_text, color_tuple, center_tuple, antialiased=True):
    # Define a message in Main Menu with Color Tuple in RGB
    msg_font = font.render(msg_text, antialiased, color_tuple)
    # Find position of the message 
    font_pos = msg_font.get_rect(center=center_tuple)
    # Draw (blit) the message at the calculated position
    screen_object.blit(msg_font , font_pos)

# Function: Check which is winner
def check_winner(player1_value, player2_value, screen_object, font_object, clock):
    frame_count = 0
    while True:
        for event in pygame.event.get():        
            # If Quit Signal is received, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen_object.fill((0,0,0))
        if frame_count < 100:
            player1_message = 'Player 1: ' + str(random.randrange(1, 5+1))
            blit_text(screen_object, font_object, player1_message, (255, 0, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            player2_message = 'Player 2: ' + str(random.randrange(1, 5+1))
            blit_text(screen_object, font_object, player2_message, (0, 0, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        elif frame_count < 200:
            player1_message = 'Player 1: ' + str(player1_value + 1)
            blit_text(screen_object, font_object, player1_message, (255, 0, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            player2_message = 'Player 2: ' + str(player2_value + 1)
            blit_text(screen_object, font_object, player2_message, (0, 0, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        elif frame_count < 300:
            winner_message = 'Player 2 wins!'
            if player1_value == player2_value:
                winner_message = 'Draw Game!'
            elif player1_value > player2_value or (player1_value == 0 and player2_value == 5):
                winner_message = 'Player 1 wins!'
            blit_text(screen_object, font_object, winner_message, (255, 255, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        else:
            break   # leave this while-loop and this function

        frame_count += 1
        pygame.display.update()
        clock.tick(FRAMES_PER_SEC)

# Function: Start the game
def start_game():
    # Initialize pygame library
    pygame.init()

    # Set default Font: comic sans
    font_object=pygame.font.SysFont('comicsans',40)    

    # Define Window Screen Display object
    screen_object = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Initial a CLOCK object to tick time
    CLOCK = pygame.time.Clock()

    # initial values
    is_reset = True

    # Game's main entry
    print('DEBUG: about to enter the game')
    while True:
        if is_reset:
            # value range: 0 - 4
            player1_value = 0
            player1_pressed_count = 0
            player2_value = 0
            player2_pressed_count = 0
            is_reset = False

        for event in pygame.event.get():
            # If Quit Signal is received, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If any key is pressed, go here
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_w]:
                player1_value = (player1_value + 1) % 5
                player1_pressed_count += 1
            if keys_pressed[pygame.K_s]:
                player1_value = (player1_value - 1 + 5) % 5
                player1_pressed_count += 1
            if keys_pressed[pygame.K_UP]:
                player2_value = (player2_value + 1) % 5
                player2_pressed_count += 1
            if keys_pressed[pygame.K_DOWN]:
                player2_value = (player2_value - 1 + 5) % 5
                player2_pressed_count += 1
            if keys_pressed[pygame.K_RETURN] and player1_pressed_count > 0 and player2_pressed_count > 0:
                check_winner(player1_value, player2_value, screen_object, font_object, CLOCK)
                is_reset = True
                
        screen_object.fill((0,0,0))

        blit_text(screen_object, font_object, 'Welcome to Number Punch!', (255, 255, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

        player1_message = 'Player 1, Press W to increase, S to decrease'
        if player1_pressed_count > 0:
            if player1_value % 2 == 0:
                player1_message = 'Player 1: @@'
            else:
                player1_message = 'Player 1: ##'
        blit_text(screen_object, font_object, player1_message, (255, 0, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))

        player2_message = 'Player 2, Press UP to increase, DOWN to decrease'
        if player2_pressed_count > 0:
            if player2_value % 2 == 0:
                player2_message = 'Player 2: @@'
            else:
                player2_message = 'Player 2: ##'
        blit_text(screen_object, font_object, player2_message, (0, 0, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))

        blit_text(screen_object, font_object, 'Press ENTER to confirm both', (255, 255, 255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 120))

        pygame.display.update()
        CLOCK.tick(FRAMES_PER_SEC)

if __name__ == '__main__':
    # Executed when invoked directly
    start_game()

    