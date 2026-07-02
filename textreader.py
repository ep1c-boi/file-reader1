#imports
import os
import json
import time

#main menu
def mainmenu():
  print("File Reader by ep1c-boi, v2")
  print(r"To use, insert a full file path 'example: C:\Users\user\Documents\note.txt'")
  file = input("Please enter file name. ")
  
  #innards
  if os.path.exists(file):
      #file viewer 
      try:
        opened = open(file)
        readed = opened.read()
        print(readed)
      #error messages
      #if its an invalid file type
      except UnicodeDecodeError:
        print("Entered path is not a text file.")
        time.sleep(5)
        os.system('cls')
        return mainmenu()
      #if the user doesnt have perms
      except PermissionError:
        print("Unauthorized to open path.")
        time.sleep(5)
        os.system('cls')
        return mainmenu()
  else:
      #fail
      print("That file doesnt exist!")
      time.sleep(5)
      os.system('cls')
      return mainmenu()


#extra
mainmenu()

