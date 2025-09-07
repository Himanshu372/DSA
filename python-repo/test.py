import pygame
import os

# Window size
WINDOW_WIDTH    = 600
WINDOW_HEIGHT   = 600
WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
    # background = pygame.transform.smoothscale(road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    windmill_image = pygame.image.load("C:\\Users\\jagta\\Desktop\\windmill_image_pygame.png").convert_alpha()
    # clock = pygame.time.Clock()
    running = True
    dt = 0
    root_dir =

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(windmill_image, (0, 0))
        pygame.display.flip()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt


        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # dt = clock.tick(60) / 1000

    pygame.quit()