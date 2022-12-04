#!/bin/python
import argparse
import os
import requests
from bs4 import BeautifulSoup


#This is a script to easily connect to the game of ssh bandit 
#https://overthewire.org/wargames/bandit
#It works on both windows and linux systems 

#Author :  Nikolasfil 


def url(num,game):
    return f"https://overthewire.org/wargames/{game}/{game}{num}.html"


def scraping(num,game):

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    request = requests.get(url(num,game),headers=header)
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

    h2='\nWith -f/--file specify the name of the report\nWith -n/--number you can specify a level to scrape \n'
    h3='\nWith -g/--game you can specify the game to construct the report(currently supporting bandit,leviathan)'

    h="This is an easy way to create a writeup for ssh wargames with each challenge\'s description.\n -g to choose either bandit or leviathan\nThe default name is going to be steps.txt and it\'s going to write for all the levels. Otherwise use -n flag for only a specific level."

    #Parser Arguments
    parser = argparse.ArgumentParser(description=h1+h2+h3)
    parser.add_argument('--file', '-f', type=str, help='File Name')
    parser.add_argument('--number', '-n', type=int, help='Scrapes Only one Level')
    parser.add_argument('--game', '-g', type=str, help='Specifies the wargame')

    args = parser.parse_args()
    
    if args.game is not None:

        if args.game=='leviathan':
            levels = 7
        elif args.game=='bandit':
            levels = 34
        
        if args.file is None:
            args.file = 'steps.txt'

        #Main excecution
        if args.number is None :  
            with open(args.file,'w') as f:
                for i in range(levels):
                    writing(f,i,args.game)

        else:
            with open(args.file,'w') as f:
                writing(f,args.number,args.game)
    
    else:
        print(h3)


if __name__=='__main__':
    main()
    
