import pygame
import time

def main():
    """ Set up the game and run the main loop. """
    pygame.init()
    count = 0           # a count to end when all the images have been shown.
    main_surface = pygame.display.set_mode((300, 220))

    # Load an image (blit)
    pics = [
    'covid_0', 'covid_1', 'covid_2', 'covid_3', 'covid_4', 'covid_5', 'covid_6', 'covid_7'] 
    imageList = []
    for i in pics:
        imageList.append(pygame.image.load(f'{i}.png'))
    i = 0 # Variable for imageList indexing.

    # Create a font for rendering text.
    my_font = pygame.font.SysFont('Courier', 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.time()

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:       # If window close button was clicked.
            break                           # Leaves the game loop.
        
        # Do other bits of logic for the game here.
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.time()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        # Completly redraw the surface starting with the background.
        main_surface.fill((0, 200, 255))

        # Draw a small red rectangle on the main surface.
        main_surface.fill((155,0,0), (300,100,150,90))

        # Copy an image to the surface at its (x, y) posn. 
        if i >= 7: 
            i = 0
        main_surface.blit(imageList[i], (30, 40))
        i += 1

        # Make a new surface with an image of the text. 
        the_text = my_font.render(
                f'Frame:{frame_count}, Rate:{frame_rate:.2f} fps.', True, (0,0,0))
        # Copy the text surface to the main surface.
        main_surface.blit(the_text, (10, 10))
        
        # Now that everything is drawn, put it on display.
        pygame.display.flip()
        # Delay to apreciate the images being shown.
        time.sleep(0.5)
        
        count += 1
        if count > len(imageList):
            pygame.quit() # has a some problems. 
    # Close the window when the loop is left
    pygame.quit()

if __name__ == '__main__':
    main()
