#Shaoyu Tang & Ying Pan
# this program create a game that let user guees a word. the user can guess one 
# letter per times. the program will show the aswer and how many chances the
# users still has so far. If the user run out of all the chances, it will be
# regarded as failed. The user will success if he/she guess the word finally
import uagame
import random
def main():
   Mywindow = uagame.Window('word puzzle', 600, 1000)  # create a window
   Mywindow.set_font_size(24)                          #set the word size in the window
   Mywindow.set_font_color('white')                    #set the word color in the window   
   list_of_words =  ['apple','banana','watermelon','kiwi','pineapple','mango'] # create the word, a list
   Word = random.choice(list_of_words)                 # random choose a word from the list
   count = 4                                           # user has 4 chances to guess at beginning
   win = False                                         # a variable used to jude whether we need to lose a chance
   y_coord = 0                                         # The y-axis of the fisrt line instructi  
   Word_list = list(Word)                              # chage word to the list
   Answer = "_" * len(Word)                            # match the length of the answer with the length of the word
   Answer_list = list(Answer)                          # change answer to the list
   
   y_coord = display_instruction(Mywindow,y_coord)     # update the y_coord
  
   # Main agorithm, creat a While loop to compare each letter in the Word list and the letter guessed by the user. If they are match, add the letter user guessed in the current postionof the Answer list.
   time = 1
   time1 = 0
   while time <= len(Word) + 4 :                # times of the loop, we cannot guess more than the number of the letter in the 
                                                # word list + 4(chances) times
      
      y_coord = show_answer_so_far(Mywindow,y_coord,Answer_list)     
      
      judge_user_win_or_lose(Mywindow,Answer_list,Word_list,Word,y_coord,count)
     
      y_coord += Mywindow.get_font_height()
      Letter = Mywindow.input_string('Guess a letter (' + str(count)+ 'guesses remaining )', 0, y_coord)    # prompt the guess, and 
                                                                                                            # show how many chances # we have
      
      win = judge_whether_the_letter_is_over_guessed_or_not(Letter,Answer_list,win,time1,Word_list)   
      
      # If the letter is over guessed, we loser one chace
      if judge_whether_the_letter_is_over_guessed_or_not(Letter,Answer_list,win,time1,Word_list) :
         count -= 1                                              
          
      win = judge_whether_the_letter_is_correct_or_not(Letter,Word_list,win,Answer_list,time1,Answer)         
     
         
         
      count = lose_chance(win,count)
         
      win =initial_the_variable(Word_list,win)
      
      time += 1

def display_instruction(Mywindow,y_coord):
      # display the instruciton  
      Instruction = ["I'm thinking of a secret word.",'Try and guess the word.You can guess one letter','at a time.Each time you guess I will show you','which letters have been correctly guessed and which','letters are still missing.You will have 4 guesses to','guesses all of the letters. Good luck!']
         
      for k in range(len(Instruction)):
         Mywindow.draw_string(str(Instruction[k]),0,y_coord)                    # dispaly each line's instruction
         if k != len(Instruction)-1 :
            y_coord += Mywindow.get_font_height()                               # find the next line
      return y_coord
   
def show_answer_so_far(Mywindow,y_coord,Answer_list):
   y_coord += Mywindow.get_font_height()  #find the y-axis of the next line   
   Mywindow.draw_string('The Answer so far is: ', 0, y_coord)                   # display the answer so far
   x_coord = Mywindow.get_string_width('The Answer so far is: ')                # display the answer after the text information
   for i in range(0,len(Answer_list)) :                                         # dialpy all the element in the answer list
      Mywindow.draw_string(str(Answer_list[i]) , x_coord, y_coord) 
      x_coord += Mywindow.get_string_width(Answer_list[i])                      # make some space between two element  
   return y_coord

def judge_user_win_or_lose(Mywindow,Answer_list,Word_list,Word,y_coord,count):
   # if the user find the word, the game will end immediately
   if Answer_list == Word_list :                                                # condition expression, user guessd all the letters
      y_coord += Mywindow.get_font_height()
      Mywindow.draw_string('Good job! You found the word '+ Word +'!' , 0, y_coord)                 
      y_coord += Mywindow.get_font_height()
      Code = Mywindow.input_string('Press enter to end the game', 0, y_coord)   # because we do not have any method to create an
      if Code == "" :                                                           # event, so we enter a empty string, it seems we
                                                                                # press the enter key and shut down the winodw
         Mywindow.close()                                                       # close the Window
        
   # if the user run out of all the chance, the gane will end immediately  
   if count == 0 :                                                              # condition expreesion, user does not have any chance
      y_coord += Mywindow.get_font_height()
      # print failed information and the word
      Mywindow.draw_string('Not quite, the correct word was '+ Word +'. Better luck next time', 0, y_coord)                        
      y_coord += Mywindow.get_font_height()   
      Code = Mywindow.input_string('Press enter to end the game', 0,y_coord)       # print an instruction to end game
      if Code == "" :                                                              # same with previous break code
         Mywindow.close()            

def judge_whether_the_letter_is_over_guessed_or_not(Letter,Answer_list,win,time1,Word_list):
   # condition expression. If the uesr guessed a same letter more than one times, it will be counted wrong     
   while time1 < len(Word_list):  
      if Letter == Answer_list[time1] : # If the letter we gueesd already is same with a letter in the Answer list, it means we alreday
                                        # guessed this letter before
            win = True                  # we do not need to lose another chance
      time1 += 1      
   return win

   
def judge_whether_the_letter_is_correct_or_not(Letter,Word_list,win,Answer_list,time1,Answer):
   # in the letter we gueessed is correct, we need to update the answer   
   while time1 < len(Word_list):     
      if Letter == Word_list[time1]:      
         win = True                        # the letter is correct, we do not need to lose a chance
         Answer_list[time1] = Letter       # add the letter into our answer
         Answer=' '.join(Answer_list)
      time1 += 1
   return win               
      

def lose_chance(win,count):
   # if we made a wrong guess,we will lose one chance
   if win == False :                                        # if we made a correct guessm the win shoule become True
      count -= 1
   return count
 
def initial_the_variable(Word_list,win):
   #afer one loop, we need to initial the judge variable                           
   win = False
   return win
   
main()
         