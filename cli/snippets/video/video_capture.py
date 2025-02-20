import cv2
import pygame
import time
"""


"""
VIDEO_FILE = 'data/mp4/blocparty_skeleton.mp4'

video_capture = cv2.VideoCapture(VIDEO_FILE)

success, img = video_capture.read()

# Get dimensions - Flips first and second element
dimensions = img.shape[1::-1]  # [height, width, ...] => [width, height]


# Display
window = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
FPS = 60  # Can control playback speed by changing fps
SPEED_MODIFIER = 0

while success:
    
    success, img = video_capture.read()
    if not success:
        break  # Video ended

    window.blit(pygame.image.frombuffer(img.tobytes(), dimensions, "BGR"), (0, 0))
    pygame.display.update()

    # Drawing Display should be done outside checking for events because then video is played back weird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            success = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right")
                SPEED_MODIFIER += 15
                SPEED_MODIFIER = min(SPEED_MODIFIER, 144)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                SPEED_MODIFIER -= 15
                SPEED_MODIFIER = max(SPEED_MODIFIER, -(FPS - 1))



    clock.tick(FPS + SPEED_MODIFIER)
    print(f"FPS: {FPS + SPEED_MODIFIER}", end='\r')

pygame.quit()
