import pygame

def draw_board(the_board):
    """ Draw a chess board with queens from the_board. """

    pygame.init()
    colors = [(255,0,0), (0,0,0)]    # set up red color

    n = len(the_board)              # total baord squares
    surface_sz = 480                # proposed physical surface size
    square_sz = surface_sz // n     # the lenght of each board square
    surface = n * square_sz         # adjust to exactly fit n squares

    # Create the surface of (width, height) and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Load queen's image.
    queen = pygame.image.load('queen.png')

    # Use an extra offset to center the queen on its square.
    # If the square is too small, offset becomes negative, but it will still be centered.
    queen_width = -1.5 + (square_sz - queen.get_width()) / 2
    queen_height = 1  +  (square_sz - queen.get_height()) / 2

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:       # If window close button was clicked.
            break                           # Leaves the game loop.

        # Draw a fresh backgroud (a black chess board)
        for row in range(n):                # Draw each row of the board.
            c_index = row % 2               # change starting color on each row
            for col in range(n):                # Run through cols drawing squares
                the_square = (col*square_sz, row*square_sz, square_sz, square_sz)
                surface.fill(colors[c_index], the_square)
                # Now flip the color index for the next square
                c_index = (c_index + 1) % 2

        # Now that the squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
            surface.blit(
                    queen,
                    #(col * square_sz, row * square_sz))
                    (col * square_sz + queen_height, row * square_sz + queen_width))

        # Now that all the elemenets have been drawn, proceed to display them.
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])

