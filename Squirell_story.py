class Nutshell:
    
    def __init__(self, place, action, result):
        self.result = result
        self.place = place     
        self.action = action
       
    
    def story(self):
        print("One day a Squirrel was searching food for her child because child was hungry. Squirell reach to the {0} and suddenly saw some piece of nutshells on ground, and Squirell takes all the piece of nutshells and gives the thanks to God and Squirell reach her home and gives the nutshells to her hungry child, Squirell {1}.\n".format(self.place, self.action))
        print(" {0} Ending ".format(self.result))




if __name__ == '__main__':
    result = input('Enter the result of story (Happy or Sad) : ')
    place = input('Enter the place name : ')
    action = input('Enter the action of Squirrel : ')
    
    obj = Nutshell(place, action, result)
    obj.story()
