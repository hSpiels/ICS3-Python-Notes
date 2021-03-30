#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries_ex1.py)
# Purpose:     This program detects a microbit and reads information from any active serial connections
#              Adapted From - https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     13-March-2021
#-----------------------------------------------------------------------------

import serial
import serial.tools.list_ports as list_ports


def findMicrobitComPort(pid=516, vid=3368, baud=115200):
    '''
    This function finds a device connected to usb by it's PID and VID and returns a serial connection

    Parameters
    ----------
    pid - Product id of device to search for
    vid - Vendor id of device to search for
    baud - Baud rate to open the serial connection at

    Returns
    -------
    Serial - If a device is found a serial connection for the device is configured and returned

    '''
    #Required information about the microbit so it can be found
    #PID_MICROBIT = 516
    #VID_MICROBIT = 3368
    TIMEOUT = 0.1
    
    #Create the serial object
    serPort = serial.Serial(timeout=TIMEOUT)
    serPort.baudrate = baud
    
    #Search for device on open ports and return connection if found
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            serPort.port = str(p.device)
            return serPort
    
    #If nothing found then return None
    return None




def main():
    print('looking for microbit')
    microbit = findMicrobitComPort()
    if not microbit:
        print('microbit not found')
        return
    
    print('opening and monitoring microbit port')
    microbit.open()

    while True:

        #Non-blocking version of serial read
        if (microbit.inWaiting()>0):
        
            #data = microbit.read(microbit.inWaiting()).decode('utf-8') #read the bytes and convert from binary array to utf-8
            data = microbit.readlines()  #Read lines into a list, one line per list entry
                  
            for i in range(len(data)): #Convert each entry in list from binary to a readable text format
                data[i] = data[i].decode('utf-8').strip()
        
        
            print(data)

#         #Blocking version of serial read
#         line = microbit.readline().decode('utf-8')
#         if line:  # If it isn't a blank line
#             print(line)
    
    microbit.close()
    
main()