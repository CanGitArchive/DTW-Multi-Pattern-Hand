import serial
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DC Motor Control")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600) # Change 'COM3' to the correct port for your system

# Function to send command to Arduino
def send_command(command):
    ser.write(command.encode())

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_command('F') # Send forward command to Arduino
            elif event.key == pygame.K_DOWN:
                send_command('B') # Send backward command to Arduino

    # Draw buttons
    forward_button = pygame.draw.rect(screen, GREEN, (00, 50, 400, 50))
    backward_button = pygame.draw.rect(screen, RED, (450, 50, 400, 50))

    # Draw button labels
    forward_text = font.render("Up arrow is Forwards", True, BLACK)
    backward_text = font.render("Down arrow is Backwards", True, BLACK)
    screen.blit(forward_text, (60, 60))
    screen.blit(backward_text, (460, 60))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
ser.close()
sys.exit()
