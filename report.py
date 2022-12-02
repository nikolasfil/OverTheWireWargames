#!/bin/python
import argparse
import os
import requests
from bs4 import BeautifulSoup


#This is a script to easily connect to the game of ssh bandit 
#https://overthewire.org/wargames/bandit
#It works on both windows and linux systems 

#Author :  Nikolasfil 


def url(num):
    return f"https://overthewire.org/wargames/bandit/bandit{num}.html"


def scraping(num):

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    request = requests.get(url(num),headers=header)
    soup = BeautifulSoup(request.text, 'html.parser')    
    text = soup.find('div',id="content")
    return text.get_text()


def writing(f,i):
    f.write(f"\n{'-'*2*len('Level 15 → Level 16')}\n\nLevel {i} → Level {i+1}\n\n{'-'*2*len('Level 15 → Level 16')}\n")
    f.write(f"{scraping(i+1)}\n")

    f.write(f'\n{"-"*len("steps: ")}\nsteps: \n\n\n{"-"*len("steps: ")}\n\n')

    f.write(f'\n{"-"*len("password: ")}\npassword: \n{"-"*len("password: ")}\n')
            





def main():
    #general command to know 
    
    h1='SSH bandit writeup with challenge\'s description'

    h2='\nWith -f/--file specify the name of the report\nWith -n/--number you can specify a level to scrape \n'

    h="This is an easy way to create a writeup for ssh bandit with each challenge\'s description\nThe default name is going to be steps.txt and it\'s going to write for all the levels. Otherwise use -n flag for only a specific level"

    #Parser Arguments
    parser = argparse.ArgumentParser(description=h1+h2)
    parser.add_argument('--file', '-f', type=str, help='File Name')
    parser.add_argument('--number', '-n', type=int, help='Scrapes Only one Level')

    args = parser.parse_args()
    if args.file is None:
        args.file = 'steps.txt'

    #Main excecution
    if args.number is None :  
        with open(args.file,'w') as f:
            for i in range(34):
                writing(f,i)

    else:
        with open(args.file,'w') as f:
            writing(f,args.number)


                
        
    



if __name__=='__main__':
    main()
    
