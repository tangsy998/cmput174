# Shaoyu Tang & Ying Pan
# This is program is a game that can show two paddles and a balls on the screen
# The ball will moving automatically.
# When the ball touch the edge of the screen, the ball will goes on the opposite 
# side of the window.

from uagame import Window
import pygame, time
from pygame.locals import *


def main():
 
   window = Window('Pong', 500, 400)                   # create a window
   game = Game(window)                                 # create a game type object
   game.play()                                         # use the paly methoes in the game class
   window.close()                                      # close the window

# User-defined classes

class Circle:
   # An object in this class represents a colored circle.

   def __init__(self, center, radius, color, window):
      # Initialize a Cirlcle.
      # - self is the Circle to initialize
      # - center is a list containing the x and y int
      # coords of the center of the Circle
      # - radius is the int pixel radius of the Circle
      # - color is the pygame.Color of the Circle
      # - window is the uagame window object

      self.center = center
      self.radius = radius
      self.color = color
      self.window = window
   
   def draw(self):
      # Draw the Circle.
      # - self is the Circle to draw
      
      pygame.draw.circle(self.window.get_surface(), self.color, self.center, self.radius) # the sequence of paramameter is from  
                                                                                          # pygame document.
                                                                                           
   
   def move(self):
      # Move the circle.
      # - self is the Circle to move
      
      window_size = (self.window.get_width(), self.window.get_height())
      for index in range(0, 2):
         self.center[index] = (self.center[index] + 10) % window_size[index] # the meaning of the moving is change the circle's postion  
                                                                             # % means find the reamining number, which is the currente position of the circle
   
  
class Game:
   # An object in this class represents a complete game.
  
   
   def __init__(self, window):
      # Initialize a Game.
      # - self is the Game to initialize
      # - window is the uagame window object
      
      self.window = window
      self.bg_color = pygame.Color('black')
      self.fg_color_str = "white"
      self.pause_time = 0.04 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      self.circle = Circle([200, 200], 20, pygame.Color(self.fg_color_str), window) # create a Circle type object 
     
     # create two paddles
      self.rectangle1 = pygame.Rect(100, 200, 10, 100)
      self.rect_color = pygame.Color('white')                                       # assignment the color 
      self.rectangle2 = pygame.Rect(300, 200, 10, 100)
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
          # play frame
         self.handle_event()
         self.draw()            
         if self.continue_game:
            self.update()
           
         time.sleep(self.pause_time) # set game velocity by pausing

 
   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled   
      event = pygame.event.poll()
      if event.type == QUIT:                                            # QUIT menas shut down all the display module
         self.close_clicked = True                                      # we can use "X" to close the window
     
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.window.clear()                    # clear the window each time, because we only need to show current psoition of the ball
                                                  
      self.circle.draw()
      pygame.draw.rect(self.window.get_surface(), self.rect_color, self.rectangle1)
      pygame.draw.rect(self.window.get_surface(), self.rect_color, self.rectangle2)
      self.window.update()                   # update the window

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      
      self.circle.move()           #let the ball moveing automatically
     
         


main()


