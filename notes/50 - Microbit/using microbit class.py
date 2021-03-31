#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries_ex1.py)
# Purpose:     This program detects a microbit and reads information from any active serial connections
#              Adapted From - https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     13-March-2021
#-----------------------------------------------------------------------------
#--------------------------EXAMPLE CODE TO RUN ON MICROBIT -------------------
# from microbit import *
# import utime
# 
# while True:
#     
#     display.show(Image.HEART)
#     print('heart ', utime.ticks_ms())
#     utime.sleep_ms(15)
# 
# 
#-----------------------------------------------------------------------------
# #
from Microbit import *


def main():
    #Create microbit instance
    mb = Microbit()
    
    #Check to make sure it's working
    if not mb.isReady():
        print('Error, Problem Loading Microbit.  Exiting Program')
        return
         

    while True:
        
        line = mb.nonBlockingReadRecentLine()
        if line != None:
            print(line)
        
    mb.closeConnection()
    
main()