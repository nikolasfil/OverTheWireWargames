#!/bin/python
import argparse
import os
import requests
from bs4 import BeautifulSoup


#This is a script to create writeups of overthewire wargames  
#https://overthewire.org/wargames/bandit
#It works on both windows and linux systems 

#Author :  Nikolasfil 

def file_existing(file):
    ls = os.listdir()
    if '.' in file:
        f = file.split('.')
        if file in ls:
            i=1
            while True:
                file = ".".join([f"{f[0]}_{i}",f[1]]) 
                if file not in ls:
                    return file
                i+=1        
    else:
        if file in ls:
            i=1
            while True:
                file = f"{file}_{i}" 
                if file not in ls:
                    return file
                i+=1
    return file

        


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



def url(num,game):
    return f"https://overthewire.org/wargames/{game}/{game}{num}.html"


def scraping(num,game):

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    request = requests.get(url(num,game),headers=header)
    soup = BeautifulSoup(request.text, 'html.parser')    
    text = soup.find('div',id="content")
    if text is not None:
        return text.get_text()


def scraping_general(game):

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    request = requests.get(f"https://overthewire.org/wargames/{game}",headers=header)
    soup = BeautifulSoup(request.text, 'html.parser')    
    text = soup.find('div',id="content")
    return text.get_text()



def writing(f,i,game):
    
    f.write(f"\n{'-'*2*len('Level 1 → Level 1')}\n\nLevel {i} → Level {i+1}\n\n{'-'*2*len('Level 15 → Level 16')}\n")
    
    f.write(f"{scraping(i+1,game)}\n")

    f.write(f'\n{"-"*len("steps: ")}\nsteps: \n\n\n{"-"*len("steps: ")}\n\n')

    f.write(f'\n{"-"*len("password: ")}\npassword: \n{"-"*len("password: ")}\n')
            





def main():
    #general command to know 
    
    h1='\nSSH wargames writeup with challenge\'s description'

    h2='\nWith -f/--file specify the name of the report (optional, there is a default value of {game}-steps.txt\nWith -n/--number you can specify a level to scrape \n'
    h3='\nWith -g/--game you can specify the game to construct the report of [leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]\n'

    
    #Parser Arguments
    parser = argparse.ArgumentParser(description=f"{h1}\n{h2}\n{h3}")
    parser.add_argument('--file', '-f', type=str, help='File Name')
    parser.add_argument('--number', '-n', type=int, help='Scrapes Only one Level')
    parser.add_argument('--game', '-g', type=str, help='Specifies the wargame')

    args = parser.parse_args()
    
    if args.game is not None:

        levels={'leviathan': 8,'krypton': 6,'bandit': 34,'natas': 34,'narnia': 9,'behemoth': 8,'utumno': 8,'maze': 9,'vortex': 27,'manpage': 7}
            
        
        if args.file is None:
            # args.file = f'{args.game}-steps.txt'
            args.file = file_existing(f'{args.game}-steps.txt')

        #Main excecution
        if args.number is None :  
            with open(args.file,'w') as f:
                clear()
                progress='Progress:[='
                f.write(f"\n{'-'*10}\n{args.game.upper()}\n{'-'*10}\n")
                progress+='='
                print(progress)
                f.write(f"{scraping_general(args.game)}\n")  
                for i in range(levels[args.game]):
                    progress+='='
                    writing(f,i,args.game)
                    clear()
                    print(progress)
                progress+=']'
                clear()
                print(progress)
            

        else:
            with open(args.file,'w') as f:
                f.write(f"\n{'-'*10}\n{args.game.upper()}\n{'-'*10}\n")
                f.write(f"{scraping_general(args.game)}\n")  
                writing(f,args.number,args.game)
    
    else:
        print(h3)


if __name__=='__main__':
    main()
    
