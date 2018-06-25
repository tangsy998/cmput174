from uagame import Window
import pygame, time, random
from pygame.locals import *

def main():
    window = Window('Memory', 800, 600)            # create a window
    game = Game(window)                            # create a game object
    game.play()                                    # play the game
    window.close()                                 # close the window
    
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
        self.init_IMAGE()
        self.save_image()      # assaigment all the images randomly
        self.cover()
        self.score = 0
    
    def init_IMAGE(self):
        # cretae a list to save the location of the image
        
        self.IMAGE = [ ] 
        for row in range(4):
            row = [ ]
            for col in range(4):
                row.append(0)                 # inital the row
            
            self.IMAGE.append(row)            # append row to IMAGE
               
    def init_grid(self):
        # create 4x4 grid of tiles
        
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
            self.draw()   
            if self.continue_game:
                self.update()
                self.decide_continue()
            time.sleep(self.pause_time) # set game velocity by pausing
                
    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled.
        pygame.event.clear(MOUSEMOTION)                # we only need the event when we click the tile
        event = pygame.event.poll()   
        if event.type == QUIT:                         # QUIT menas shut down all the display module
            self.close_clicked = True                  # we can use "X" to close the window
  
        if event.type == MOUSEBUTTONDOWN:              # when the user express the mouse button
            self.handle_mouse_event(event)
            
             
    def handle_mouse_event(self, event):
        # display the image at the postion where user clicked
        
        screen_height = self.window.get_height()
        screen_width  = self.window.get_width() 
        pos = event.pos                                      # get the mouse's position
        if (pos[0] > 0 and pos[0] < (4*screen_width//5)):    # we do not need to click the positon where do not have tiles
            for row in self.grid:
                for tile in row:
                
                    if tile.is_filled():             # we only need to clik the postion where the image are not show
                    
                        if tile.select(event.pos):
                            self.IMAGE[pos[1] // (screen_height//4)][pos[0] // (screen_width//5)] = pygame.transform.scale(self.IMAGE[pos[1] // (screen_height//4)][pos[0] // (screen_width//5)], (screen_width//5 -2, screen_height//4-2))   
                            self.surface.blit(self.IMAGE[pos[1] // (screen_height//4)][pos[0] // (screen_width//5)],(tile.left, tile.top))
                       
                            tile.not_filled()       # after we click the tils, we do not need click it second times
                   
                        
    def load_image(self):
        #load each image 2 times
      
        for i in range(0,16):
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
                   
    def cover(self):
        # overlap all the tile when the game start
        
        for row in self.grid:
            for tile in row:
                
                tile.draw()
                tile.draw_content()
        
    def save_image(self):
        # assignment the postion to each image 
        # - self is the Game to draw
        self.load_image()
        screen_height = self.window.get_height()
        screen_width  = self.window.get_width()        
        ran = [ ] 
        for row in self.IMAGE:
            for col in range(len(row)):
               
               # judge each image only load 2 times
                load = True
                while load == True:
                    ran_num = random.randint(0,15)
                    ran.append(ran_num)
                    count = 0    
                    for col_num in range(len(ran)):
                        if ran[col_num]== ran_num:
                            count += 1 
                            
                    if count <= 1 :            # the image only load 0 or 1 time before  
                        row[col] = self.image[ran_num]
                        load = False
                       
    def draw(self):
        # draw all the game object
        
        self.draw_score()  
        self.window.update()
    
    def draw_score(self):
        # draw score on the window
        
        self.window.set_font_size(80)
        self.window.set_font_color('white')
        if self.score < 10 :
            self.window.draw_string(str(self.score), 770, 0)
        elif self.score < 100:
            self.window.draw_string(str(self.score), 740, 0)
        else:
            self.window.draw_string(str(self.score), 710, 0)
            
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        self.window.update()
        self.score = pygame.time.get_ticks() // 1000
                 
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        # if all the images are exposed, the game will stop
        
        count = 0
        for row in self.grid:
            for tile in row:
                if not tile.is_filled():      # if the iamge already exposed, the method will return False
                    count += 1

        if count == 16:                       # All the image are exposed
            self.continue_game = False
                
class Tile():
    def __init__(self, window, size, location):
        # initalize a Tile 
        
        self.window = window
        self.left = location[0]
        self.top = location[1]
        self.width = size[0]
        self.height = size[1]
        self.rectangle = pygame.Rect(self.left, self.top, self.width, self.height)      
        self.fg_color =  pygame.Color('black')
        self.border_width = 2
        self.content = ''
       

    
    def draw_content(self):
        # assignment a content to each tile
        
        self.content = '?'       # '?' meas we do not know the image at this postion

    def draw(self):
        # display the image at the position
        
        surface = self.window.get_surface()
        image = pygame.image.load('image0.bmp')
        image = pygame.transform.scale(image, (self.width,self.height))
        surface.blit(image, (self.left,self.top))
        pygame.draw.rect(self.window.get_surface(),  self.fg_color, self.rectangle, self.border_width)
           
    
    def is_filled(self):
        #judge whether we know the image at that position or not
        
        if self.content == '?':                  # we do not know the image at that position
            return True
    def not_filled(self): 
        # change the content because we already know the image at that position
        
        self.content = ''
        
    def select(self, pos):
        # a method to selcet the tile
        
        if pos[0] > self.rectangle.left and pos[0] < (self.rectangle.left+self.rectangle.width):
            if pos[1] > self.rectangle.top and pos[1] < (self.rectangle.top + self.rectangle.height ):  
                if self.is_filled():
                    return True
      

main()