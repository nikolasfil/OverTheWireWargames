#!/bin/python
import argparse
import os

#This is a script to easily connect to the game of ssh bandit 
#https://overthewire.org/wargames/bandit
#It works on both windows and linux systems 

#Author :  Nikolasfil 


def clear():
    #yes there is a more efficient way 
    #to discern os
    try:
        os.system('clc')
    except:
        pass 

    try :
        os.system('clear')
    except : 
        pass  

def welcomingMessage(msg,sl=0):
    clear()   
    print(msg)
    
    if sl!=0:
        __import__("time").sleep(sl)
        clear()
    

def main():
    #general command to know 
    command = "ssh bandit_@bandit.labs.overthewire.org -p 2220"
    com1 = "ssh bandit"
    com2 = "@bandit.labs.overthewire.org -p 2220"

    h1='SSH bandit easy connect'

    h2='\nwith -n you can specify a level to play \nwith -c you can specify a level to start and loop through all the rest \nYou can break out of the loop with keyboardInterruption at the continue to level prompt'

    h="This is an easy way to connect to the game ssh bandint,by overthewire \nhttps://overthewire.org/wargames/bandit/\n"

    #Parser Arguments
    parser = argparse.ArgumentParser(description=h1+h2)
    parser.add_argument('--number', '-n', type=int, help='Individual Level Number')
    parser.add_argument('--cycle', '-c', type=int, help='Starts going through all the levels starting with c')
    args = parser.parse_args()


    #Main excecution
    if args.cycle is None and args.number is not None:  
        welcomingMessage(h,2)
        os.system(com1 + str(args.number) + com2)

    elif  args.cycle is not None and args.number is  None:
    
        welcomingMessage(h,2)
        num = args.cycle
    
        while num < 32:
    
            try:
                x = input(f'Press Enter to continue to lelel:{num}')    
                clear()
                os.system(com1 + str(num) + com2)
                num += 1
    
            except KeyboardInterrupt:
                break
        
    elif args.cycle is None and args.number is None:
        welcomingMessage(h)
        print(h2)

    elif args.cycle is not None and args.number is not None:
        welcomingMessage(h)
        print(h1+h2+"\n\nYou have to specify only one option ")
    

if __name__=='__main__':
    main()

