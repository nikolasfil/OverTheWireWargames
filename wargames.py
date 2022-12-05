#!/bin/python
import argparse
import os

#This is a script to easily connect to the game of ssh wargame 
#https://overthewire.org/wargames/wargame
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
    wargames={'leviathan': 2223,'krypton': 2231,'bandit': 2220,'natas': 34,'narnia': 2226,'behemoth': 2221,'utumno': 2227,'maze': 2225,'manpage': 2224}
        
    command =lambda game,level: f"ssh {game}{level}@{game}.labs.overthewire.org -p {wargames[game]}"
    
    h1='OverTheWire wargames easy connect.\n\n'

    h2='\nWith -n you can specify a level to play \nor with -c you can specify a level to start and loop through all the rest.\nWith -g you must choose between [leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]\nYou can break out of the loop with keyboardInterruption at the continue to level prompt'

    h="This is an easy way to connect to the overthewire wargames \nhttps://overthewire.org/\n"

    #Parser Arguments
    parser = argparse.ArgumentParser(description=h1+h2)
    parser.add_argument('--number', '-n', type=int, help='Individual Level Number')
    parser.add_argument('--cycle', '-c', type=int, help='Starts going through all the levels starting with c')
    
    parser.add_argument('--game', '-g', type=str, help='Choose between bandit and wargame')
    
    args = parser.parse_args()


    #Main excecution
    if args.game in wargames.keys():
        args.game=args.game.lower()
        levels={'leviathan': 8,'krypton': 6,'bandit': 34,'natas': 34,'narnia': 9,'behemoth': 8,'utumno': 8,'maze': 9,'vortex': 27,'manpage': 7}
                    
        

        if args.cycle is None and args.number is not None:  
            welcomingMessage(h,2)
            os.system(command(args.game,args.number))

        elif  args.cycle is not None and args.number is  None:
        
            welcomingMessage(h,2)
            num = args.cycle
            

            while num < levels[args.game]:
        
                try:
                    x = input(f'Press Enter to continue to level{num}: ')    
                    clear()
                    os.system(command(args.game,num))
                    num += 1
        
                except KeyboardInterrupt:
                    break
            
        elif args.cycle is None and args.number is None:
            welcomingMessage(h)
            print(h2)

        elif args.cycle is not None and args.number is not None:
            welcomingMessage(h)
            print(h1+h2+"\n\nYou have to specify only one option ")

    elif args.game is None: 
        print('Choose -g [leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]')
    
    elif args.game not in wargames.keys(): 
        print(f'\n{args.game} is not supported.\nChoose one of the games : leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage')
        

if __name__=='__main__':
    main()