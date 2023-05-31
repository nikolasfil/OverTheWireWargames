# Overthewire SSH wargame 

------------------------

*Requirements:*

python3.6 or newer 

ssh-client (for the wargames.py)

pip3 

------------------------

**wargames.py**

A simple script to automate the process of connecting to the different levels of the overthewire.org/wargames/
Supporting all the games of overthewire


It can run without any requirements and takes three parsing options:

```Bash
-g / --game #[leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage] , required

-n / --number #and following up with and integer . This connects to the ssh level you specify with the integer , option 1 

-c / --cycle #and following up with an integer , you start with the level you specify and then it continues on as a loop for the rest of the levels , option 2 

-p / --password #if flagged it will prompt to save the passwords and display the ones that have been saved in a {game}-passwords.txt file in the same folder and copies the password for the next challenge in clipboard , optional 
```

You must always specify -g and select either -c or -n.
-p is optional , and it does not need any additional argument 

It works for any os 

With --game/-g you specify which game you want to load. The script is automatically using the right port and adress for ssh to connect.

About --cycle/-c level (integer) , start from the level you specify, and connect to ssh. After exiting the ssh, there is a prompt so you can either exit with ctr+c (keyboard interrupt) or pressing ENTER to continue to the next

With --number/-n level(integer) , it connects to the specific level of the challenge.

With --password/-p no argument , it creates a password file if it doesnt exist, and everytime you go to a level it prompts you to save the password , which is then saved to the file . If the password file exists, and you are logging into a level you have a saved password, it will print the password to the screen so you can copy it and paste it in the login. Otherwise if you are logging into a level you don't have a password saved, it will ask you if you have a password to save or just continue to the level.
Also for systems that have a clipboard service running, the password for the next level is going to be copied with pyperclip


The wargames.py can run with just -g and -p , and it will run the default with cycles, by getting the passwords saved and loading the last level saved, or starting the challenge from 0 



Usage:

Running a game from starting_level till it is stopped, without prompting for passwords

```Bash
python wargames.py -g game -c starting_level
```

Running a game on a specific level , without prompting for passwords

```Bash
python wargames.py -g game -n specific_level 
```


Running a game on a specific level ,printing and saving passwords

```Bash
python wargames.py -g game -n specific_level -p 
```

Running a game from starting_level till it is stopped, printing and saving passwords

```Bash
python wargames.py -g game -c starting_level -p
```

Running a game from the last saved password

```Bash
python wargames.py -g game -p 
```


This initiates the ssh connection and off to the fun !!

------------------------


**report.py**

A simple script that scrapes the challenge's description off the site.

To use it first install the requirements

```Bash
pip3 install -r requirements.txt
```

or simply 

```Bash
pip3 install beautifulsoup4
pip3 install requests
pip3 install pyperclip
```


It takes three arguments:

```Bash
-g / --game #[leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]

-f / --file #for the name of the file.(optional) Default value is {game}-steps.txt

-n / --number #to specify the level to scrape (optional). If number is not specified it will create a steps for all the levels.
```

Usage:

```Bash
python report.py -g game 

python report.py -g game -f filename

python report.py -g game -n level_number

python report.py -g game -f filename -n level_number

```

 
------------------------

bandit-steps.txt  is the complete scraping you would get by using the -g bandit

The script will automatically create a file_{number} if you already have a file named the same as the -f .

-----------------------

Examples

```Bash
python report.py -g krypton

```
This creates krypton-steps.txt, with the game's description and all the level description, including a field for including your steps and password 

```Text
-------
steps:


-------


----------
password:
----------

```


