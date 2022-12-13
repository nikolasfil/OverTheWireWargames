#!/bin/python
import argparse
import os
import time
import platform
import pyperclip


#https://overthewire.org/wargames/wargame
#last updated 14/12/2022 - 00:05

#Author :  Nikolasfil 

class WarGames:
    def __init__(self):
        
        self.wargames={'leviathan': 2223,'krypton': 2231,'bandit': 2220,'natas': 34,'narnia': 2226,'behemoth': 2221,'utumno': 2227,'maze': 2225,'manpage': 2224}
        
        self.welcoming_message='OverTheWire wargames easy connect.\n\n'

        self.options_message='\nWith -n you can specify a level to play \nor with -c you can specify a level to start and loop through all the rest.\nWith -g you must choose between [leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]\nYou can break out of the loop with keyboardInterruption at the continue to level prompt'

        self.usage_message="This is an easy way to connect to the overthewire wargames \nhttps://overthewire.org/\n"
       
        self.levels={'leviathan': 8,'krypton': 8,'bandit': 34,'natas': 34,'narnia': 9,'behemoth': 8,'utumno': 8,'maze': 9,'vortex': 27,'manpage': 7}
        self.passwords={}
                    

    def clear(self):
        if 'linux' in platform.system().lower() or 'darwin' in platform.system().lower() :
            os.system('clear')
        if 'windows'in platform.system().lower():
            os.system('clc')



    def message(self,msg,time_sleep=0):
        self.clear()   
        print(msg)
        
        if time_sleep!=0:
            time.sleep(time_sleep)
            self.clear()

    
    def password_manager(self):
        file = f"{self.args.game}-passwords.txt"
        ls = os.listdir()
        if file not in ls:
            with open(file,'w') as f :
                f.write('')
        with open(file,'r') as f :
            ls = [i.strip('\n') for i in f ]
        self.passwords={ls[i]:ls[i+1] for i in range(0,len(ls)-1,2)}
        

    def password_saver(self):
        n = str(self.args.cycle if self.args.cycle is not None else self.args.number) 
        if n in self.passwords.keys():
            print(f'\nPassword for next level is: {self.passwords[n]}\n')
            pyperclip.copy(self.passwords[n])


        #  todo : create the file if the file does not exist!!!
        
        with open(f"{self.args.game}-passwords.txt",'w') as f:
            for i,v in self.passwords.items():
                if i is not None and v is not None:
                    f.write(f"{i}\n{v}\n")
        
        if n in self.passwords.keys():
            x =input('\n\n Press enter to continue: ') 
        else:
            password=input('\n\n Type the password for the next level or press enter to continue: ')
            if password!='' and password!='\n':
                self.passwords[self.args.cycle if self.args.cycle is not None else self.args.number]=password
        
        # sth is off with the passwords when writting the same file
        with open(f"{self.args.game}-passwords.txt",'w') as f:
            for i,v in self.passwords.items():
                if i is not None and v is not None:
                    f.write(f"{i}\n{v}\n")


    def command(self):
        return f"ssh {self.args.game}{self.args.cycle if self.args.cycle is not None else self.args.number}@{self.args.game}.labs.overthewire.org -p {self.wargames[self.args.game]}"


    def parsing_arguments(self):
        #Parser Arguments
        parser = argparse.ArgumentParser(description=self.welcoming_message+self.options_message)
        parser.add_argument('--number', '-n', type=int, help='Individual Level Number')
        parser.add_argument('--cycle', '-c', type=int, help='Starts going through all the levels starting with c')
        
        parser.add_argument('--game', '-g', type=str, help='Choose between bandit and wargame')
        parser.add_argument('--password', '-p',default=False,action='store_true',help='Save passowrds')
        
        
        self.args = parser.parse_args()       


    def running_cycles(self):
        # self.message(self.usage_message,2)

        while self.args.cycle < self.levels[self.args.game]:
            
            try:  
                self.clear()
                if self.args.password is not None and self.args.password:                    
                    self.password_saver()
                else:
                    x = input(f'\nPress Enter to continue to level{self.args.cycle if self.args.cycle is not None else self.args.number}: ')    
                os.system(self.command())
                self.args.cycle += 1
    
            except KeyboardInterrupt:
                break

    def main(self):
        
        self.parsing_arguments()

        #Main excecution
        if self.args.game is not None and self.args.game.lower() in self.wargames.keys():
            
            self.args.game=self.args.game.lower()
            
            if self.args.password is not None and self.args.password:
                self.password_manager()
                

            if self.args.cycle is None and self.args.number is not None:  
                # Running a specific level
                if self.args.password is not None and self.args.password:                    
                    self.password_saver()
                os.system(self.command())
                
            elif  self.args.cycle is not None and self.args.number is None:
                # Running the cycles
                self.running_cycles()
                
            elif self.args.cycle is None and self.args.number is None:
                # Ran the progarm without arguments
                self.message(self.usage_message+self.options_message)

            elif self.args.cycle is not None and self.args.number is not None:
                # ran the program with both arguments 
                self.message(self.welcoming_message+self.options_message+"\n\nYou have to specify only one option ")

        elif self.args.game is None: 
            # didnt specify a game
            self.message('Choose -g [leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]')
        
        elif self.args.game not in wargames.keys(): 
            # Game not supported 
            self.message(f'\n{self.args.game} is not supported.\nCuhoose one of the games : leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage')
            

if __name__=='__main__':
    app = WarGames()
    app.main()