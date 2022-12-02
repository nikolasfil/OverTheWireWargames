# SSHBandit
Overthewire ssh bandit wargame 

bandit.py is a simple script to automate the process of connecting to the different levels of the overthewire.org/wargames/bandit/

bandit.py can take two parsing options

Either -n / --number and following up with and integer . This connects to the ssh level you specify with the integer 

With -c / --cycle and following up with an integer , you start with the level you specify and then it continues on as a loop for the rest of the levels 

It is working for both windows and linux 

------------------------

report.py is a simple script that scrapes the challenge's description off the site.

report.py can take two arguments

-f/--file for the name of the file. Default value is steps.txt

-n/--number to specify the level to scrape

------------------------

bandit-steps.txt  is the complete scraping you would get by using the -f flag

