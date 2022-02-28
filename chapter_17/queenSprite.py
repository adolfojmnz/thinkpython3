import pygame
from duke_spritesheet import DukeSprite

gravity = 0.1

class QueenSprite:

    def __init__(self, image, target_posn):
        """ Create and initialize a queen 
            for this target position on the board. 
        """
        self.image = image
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)                          # start queen at top of its column. 	  
        self.y_velocity = 0        	            # initial velocity.
                                                                                        
    def update(self):                                                                   
        self.y_velocity += gravity 	            # gravity changes the velocity.
        (x, y) = self.posn                                                                       
        new_y_pos = y + self.y_velocity             # velocity moves the queen,
        (target_x, target_y) = self.target_posn     # unpack the position.
        self.posn =(x, new_y_pos)                   # to this new position.             
        dist_to_go = target_y - new_y_pos           # How far to the floor.

        if dist_to_go < 0:                          # if on floor.
            self.y_velocity = -0.65 * self.y_velocity # bounce.
            new_y_pos = target_y + dist_to_go       # move back above the floor.

        self.posn = (x, new_y_pos)                  # set the new position. 
        return                                                                         
                                                                                       
    def draw(self, target_surface):                 # draw queen at a target position.
        target_surface.blit(self.image, self.posn)

    def contains_point(self, p):
        """ 
        Returns True if the sprite rectangle contais the point p. 
        """
        (coord_x, coord_y) = self.posn              # sprite's origin.
        sprite_width = self.image.get_width()       # the extension on the x axis.
        sprite_height = self.image.get_height()     # the extension on the y axis.
        (x, y) = p                                  # unpack the point tuple.

        # The point x coord most be between the sprite x coord and its maximun width.
        inside_width = (x >= sprite_width and x < sprite_width) 
        # The point y coord most be between the sprite y coord and its maximun height.
        inside_height = (y >= sprite_height and y < sprite_height)
        return inside_width and inside_height

    def handle_click(self):
        self.y_velocity += 5.0                      # Kick it up!

def draw_board(the_board):
    """ Draw a chess board with queens from the_board. """

    clock = pygame.time.Clock()
    
    pygame.init()
    RGB_brown = (133,94,66)
    RGB_white = (255,255,255)
    RGB_black = (24,26,24)
    colors = [RGB_brown, RGB_black]      # set up a black and brown background. 
                                                                               
    n = len(the_board)                      # total baord squares  
    surface_sz = 480                        # proposed physical surface size
    square_sz = surface_sz // n             # the lenght of each board square 
    surface = n * square_sz                 # adjust to exactly fit n squares

    # Create the surface of (width, height) and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Load queen's image.

    queen = pygame.image.load('/home/adolfoj/Dev/thinkpython3/src/Chapter_17/queen_chess.png')

    # Use an extra offset to center the queen on its square.
    # If the square is too small, offset becomes negative, but it will still be centered.
    queen_width = -1.5 + (square_sz - queen.get_width()) / 2
    queen_height = 1  +  (square_sz - queen.get_height()) / 2

    all_sprites = []                        # keep a list of all sprites in the game.

    # Create a sprite object for each queen and populate the sprite list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(queen,
                    (col * square_sz + queen_height, row * square_sz + queen_width))
        all_sprites.append(a_queen) 

    # Load the sprite sheet
    duke_sprite_sheet = pygame.image.load("/home/adolfoj/Dev/thinkpython3/src/Chapter_17/duke_spritesheet.png")
    
    # Instantiate two duke instances, put them on the chessboard
    duke1 = DukeSprite(duke_sprite_sheet,(square_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet,(square_sz*5, square_sz))

    # Add them to the list of sprites which our game loop manages
    all_sprites.append(duke1)
    all_sprites.append(duke2)

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:      	# if window close button was clicked.
            break;                         	# leaves the game loop.

        if event.type == pygame.KEYDOWN:        # if an keyboard key have been pressed.
            key = event.dict['key']
            if key == 27:                       # if the scape key have been pressed.
                break                           # leave the game loop.
            elif key == ord('w'):
                colors[0] = RGB_white           # Change to white color.
            elif key == ord('b'):
                colors[0] = RGB_brown           # Change to brown color. 
                
        if event.type == pygame.MOUSEBUTTONDOWN: # if clicked the mouse.
            click_posn = event.dict['pos']      # click point coordinates.
            print('Mouse button was clicked')
            for sprite in all_sprites:
                if sprite.contains_point(click_posn): # check if one of the sprites was clicked.
                    sprite.handle_click()       # call for the corresponding method.
                    print('it pass through handle_click() method')
                    break

        if event != pygame.NOEVENT:             # print only if it is interesting!
            print(event)
        
        # Ask for every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        # Draw a fresh backgroud (a black chess board)
        for row in range(n):                # draw each row of the board.
            c_index = row % 2               # change starting color on each row
            for col in range(n):            # Run through cols drawing squares
                the_square = (col*square_sz, row*square_sz, square_sz, square_sz)
                surface.fill(colors[c_index], the_square)
                # Now flip the color index for the next square 
                c_index = (c_index + 1) % 2

        # Ask every sprite to draw itsef.
        for sprite in all_sprites:
            sprite.draw(surface)

        # Now that all the elemenets have been drawn, proceed to display them.
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    
