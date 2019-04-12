# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:37:57 2019

@author: Yansong Tu @ SUTPC

"""

# convert time section to index
def timesec2index(timesec):
    hour = int(timesec[0] + timesec[1])
    minute = int(timesec[2] + timesec[3])
    #second = int(timesec[4] + timesec[5])
    minute_floor = minute//5
    print("You may look it up in file with index", hour*12 + minute_floor+1)
 
# convert index to time section
def index2timesec(index):
    hour = (int(index)-1)//12
    minute = (int(index)-1)%12
    if hour < 10 and minute*5 < 10:
        str_start = "0" + str(hour) + ":0" + str(minute*5) + ":" + "00"
        str_end = "0" + str(hour) + ":0" + str(minute*5+4) + ":" + "59"       
    elif hour < 10: 
        str_start = "0" + str(hour) + ":" + str(minute*5) + ":" + "00"
        str_end = "0" + str(hour) + ":" + str(minute*5+4) + ":" + "59"        
    elif minute*5 < 10:
         str_start = str(hour) + ":0" + str(minute*5) + ":" + "00"
         str_end = str(hour) + ":0" + str(minute*5+4) + ":" + "59"
    else:
        str_start = str(hour) + ":" + str(minute*5) + ":" + "00"
        str_end = str(hour) + ":" + str(minute*5+4) + ":" + "59"
    s = "The given index refers to the time section from {0} to {1}."
    print(s.format(str_start, str_end))
    main()

def main():
    print("\n")
    print("--- NOTE: Type e to exit the program and/or restart the kernel. --- \n")
    u_input = input("Please type in your time section or index below: \n")
    if u_input == 'e':
        exit()
    elif u_input.isdigit():
        if 0 < len(u_input) <= 3 and int(u_input) <= 288: 
            index2timesec(u_input)
        elif len(u_input) == 6 and int(str(u_input[0] + u_input[1])) < 24 and int(str(u_input[2] + u_input[3])) < 60 and int(str(u_input[4] + u_input[5])) < 60:
            timesec2index(u_input)
        else:
            print("This is not a valid input. \n")
            print("Please review the message printed above in greater detail.\n")
            main()
    else:
        print("This is not a valid input. \n")
        print("Please review the message printed above in greater detail.\n")
        main()
        
print("If you wish to type in a time section, \n") 
print("please type it in with the following format: \n")
print(" 'hh+mm+ss' ex. '140325' or '000428'. \n")
print("\n")
print("If you wish to type in a time index, \n")
print("please type it in directly. \n")
main()
