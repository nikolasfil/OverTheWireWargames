# Overthewire SSH wargame 

wargames.py is a simple script to automate the process of connecting to the different levels of the overthewire.org/wargames/
Currently supporting bandit and leviathan

It takes three parsing options:

```Bash
-g / --game #leviathan or bandit,and

-n / --number #and following up with and integer . This connects to the ssh level you specify with the integer 

-c / --cycle #and following up with an integer , you start with the level you specify and then it continues on as a loop for the rest of the levels 
```

You must select either -c or -n , and always specify -g 

It is working for both windows and linux 

------------------------

report.py is a simple script that scrapes the challenge's description off the site.

It takes three arguments:

```Bash
-g / --game #leviathan or bandit (must)

-f / --file #for the name of the file.(optional) Default value is steps.txt

-n / --number #to specify the level to scrape (optional). If number is not specified it will create a steps for all the levels.
```

------------------------

bandit-steps.txt  is the complete scraping you would get by using the -f flag
Leviathan challenge does not have 
