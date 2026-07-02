#imports
import os
import json
import time

#main menu
def mainmenu():
  print("File Reader by ep1c-boi, V1")
  print(r"To use, insert a full file path 'example: C:\Users\user\Documents\note.txt'")
  file = input("Please enter file name. ")
  
  #innards
  if os.path.exists(file):
      #file viewer
      opened = open(file)

      readed = opened.read()
      print(readed)
  else:
      #fail
      print("That file doesnt exist!")
      time.sleep(5)
      os.system('cls')
      return mainmenu()


#extra
mainmenu()
