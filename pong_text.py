# Shaoyu Tang & Ying Pan
# This is program is a game that can show two paddles and a balls on the screen
# The ball will moving automatically.
# When the ball touch the edge of the screen, the ball will bounce off the window edges and it should bounce off the front side of 
# each paddle but go through the back side of each paddle.
# the game will shut down when the score reaches to 11
from uagame import Window
import pygame, time
from pygame.locals import *

# User-defined functions

def main():
  
   window = Window('Pong', 500, 400)          # create a window           
   game = Game(window)                        # create a game type object
   game.play()                                # play the game
   window.close()                             # close the window

# User-defined classes

class Circle:
   # An object in this class represents a colored circle.
 
   def __init__(self, center, radius, color, window,speed):
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
      self.speed = [5,5]                  # assignment a speed for the ball
      self.score = [0,0]                  # inital the score for each user
     
   
   def draw(self):
      # Draw the Circle.
      # - self is the Circle to draw
      
      pygame.draw.circle(self.window.get_surface(), self.color, self.center, self.radius)
   
   
     
   def move(self):
      # Move the circle.
      # - self is the Circle to move
      window_size = (self.window.get_width(), self.window.get_height())
      for index in range(0, 2):
         self.center[index] += self.speed[index]                           # moving the ball
      
         if self.center[index] >= window_size[index] - self.radius:        # if the ball touch the right and bottom edge, the ball 
            self.speed[index] = -self.speed[index]                         # will bounce off
            
         
         elif self.center[index] <=  self.radius:                          # if the ball touch the left and top edge, the ball will 
            self.speed[index] = -self.speed[index]                         # bounce off
         
         
         # the ball will bounce off, if it touch the front side of the paddles 
         if self.center[0] == 110 + abs(self.speed[0]) or self.center[0] == 400 - abs(self.speed[0]):  # confirm that the ball touch 
            self.center[index] += self.speed[index]                                                    # the paddle from the front
         
            if self.center[0] == 110 or self.center[0] == 400:                                         # the ball touch the paddles
               if self.center[1] >= 200 and self.center[1] <= 250 :                                    
                  self.speed[index] = -self.speed[index]                                               # bounce off
                  
   def Score(self):
      # judge the score, if the ball touch the left edge, the right user get one score. simliar thing for the left user
      if self.center[0] <= self.radius :                                                                                       
         self.score[1] += 1
    
      if self.center[0] >= self.window.get_width()- self.radius:
         self.score[0] += 1
      
   def draw_score(self):
      # display the score
      self.window.set_font_size(96)
      self.window.draw_string(str(self.score[0]),0,0)
      self.window.draw_string(str(self.score[1]), 420,0)
  
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
      self.circle = Circle([370, 200], 5, pygame.Color(self.fg_color_str), window, [5,5])
      self.elapsed_time = 0
      
      # create two paddles
      self.rectangle1 = pygame.Rect(100, 200, 10, 50)
      self.rect_color = pygame.Color('white')               # assignment the color
      self.rectangle2 = pygame.Rect(400, 200, 10, 50)
         
      
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
      if event.type == QUIT:                         # QUIT menas shut down all the display module
         self.close_clicked = True                   # we can use "X" to close the window
         
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      if self.continue_game == True:              
         self.window.clear()                     # clear the window each time, because we only need to show current psoition of the ball
         self.circle.draw()
         pygame.draw.rect(self.window.get_surface(), self.rect_color, self.rectangle1)
         pygame.draw.rect(self.window.get_surface(), self.rect_color, self.rectangle2)
         self.circle.draw_score()
         self.window.update() 
         
      # By the rule, the game will stop when one of player's score reaches 11        
      if self.circle.score[0] == 11 or self.circle.score[1] == 11:
         self.continue_game = False              # when one player win the game, we do not update the game                

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      self.circle.move()                      # Let the ball move automatically
      self.circle.Score()                     # Let prgram judge the score
      
main()


