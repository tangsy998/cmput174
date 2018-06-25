from uagame import Window
import pygame, time, random
from pygame.locals import *

def main():
    window = Window('Memory', 800, 600)           # create a window
    game = Game(window)                           # create a game object
    game.play()                                   # play the game
    window.close()                                # close the window

# User-defined classes
    
class Game:
    # An object in this class represents a complete game.
    
    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame window object
            
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.image = [] 
        self.surface = window.get_surface()
        self.init_grid()
        self.draw()
        
    def init_grid(self):
        # create 3x3 grid of tiles
        screen_height = self.window.get_height()
        screen_width  = self.window.get_width()
        tile_size = (screen_width//5, screen_height//4)
        self.grid = [ ]
        for row_num in range(4):
            row = [ ]
            for col_num in range(4):
                # create tile
                tile_location = (col_num * screen_width // 5, row_num * screen_height//4)
                tile = Tile(self.window, tile_size, tile_location)
                row.append(tile)               # append tiles to row
                        
            
            self.grid.append(row)              # append rows to grid  
    
    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
    
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_event()
                      
            if self.continue_game:
                self.update()
                self.decide_continue()
            time.sleep(self.pause_time) # set game velocity by pausing
                
    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled.
    
        event = pygame.event.poll()   
        if event.type == QUIT:                         # QUIT menas shut down all the display module
            self.close_clicked = True                   # we can use "X" to close the window
  
        
            
           
    def load_image(self):
        # load image 
        for i in range(0,16):
            
            # append each image 2 times 
            if i % 8 == 0:
                self.image.append(pygame.image.load('image1.bmp'))  
                
            if i % 8 == 1:
                self.image.append(pygame.image.load('image2.bmp'))
              
            if i % 8 == 2:
                self.image.append(pygame.image.load('image3.bmp'))
               
            if i % 8 == 3:
                self.image.append(pygame.image.load('image4.bmp'))
                
            if i % 8 == 4:
                self.image.append(pygame.image.load('image5.bmp'))
                
            if i % 8 == 5:
                self.image.append(pygame.image.load('image6.bmp'))
               
            if i % 8 == 6:
                self.image.append(pygame.image.load('image7.bmp'))
                
            if i % 8 == 7:
                self.image.append(pygame.image.load('image8.bmp'))
            
        
        
    def draw(self):
        # Draw all the images.
        # - self is the Game to draw
        self.load_image()
        screen_height = self.window.get_height()
        screen_width  = self.window.get_width()        
        ran = [ ] 
        for row in self.grid:
            for tile in row:
                tile.draw()
                
                # judge each image only load 2 times
                load = True
                while load == True:
                    ran_num = random.randint(0,15)
                    ran.append(ran_num)
                    count = 0 
                    
                    for cou in range(len(ran)):
                        if ran[cou]== ran_num:
                            count += 1 
                      
                    if count <= 1 :            # the image only load 0 or 1 time before     
                        self.image[ran_num] = pygame.transform.scale(self.image[ran_num],(screen_width//5, screen_height//4))
                        self.surface.blit(self.image[ran_num],((tile.left, tile.top)))
                        load = False
                    
 
        self.window.update()                    # update all the object
            
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        # in this version we do not need to update game object automatically
        pass
                 
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        # in this version, we do not need to conseider whether we to continue the game or not   
        pass

   

class Tile():
    def __init__(self, window, size, location):
        # initalize a Tile 
        
        self.window = window
        self.left = location[0]
        self.top = location[1]
        width = size[0]
        height = size[1]
        self.rectangle = pygame.Rect(self.left, self.top, width, height)      
        self.fg_color =  pygame.Color('black')
        self.border_width = 5

    
    
    def draw(self):
        # draw border for each tile.
        pygame.draw.rect(self.window.get_surface(),  self.fg_color, self.rectangle, self.border_width)
    
    
main()