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
-g / --game #[leviathan,krypton,bandit,natas,narnia,behemoth,utumno,maze,vortex,manpage]

-n / --number #and following up with and integer . This connects to the ssh level you specify with the integer 

-c / --cycle #and following up with an integer , you start with the level you specify and then it continues on as a loop for the rest of the levels 

-p / --password #if flagged it will prompt to save the passwords and display the ones that have been saved in a {game}-passwords.txt file in the same folder and copies the password for the next challenge in clipboard
```

You must select either -c or -n , and always specify -g 
-p is optional , and it does not need any additional argument 

It works for any os 

Usage:

```Bash
python wargames.py -g game -c starting_level
```

```Bash
python wargames.py -g game -n specific_level 
```

```Bash
python wargames.py -g game -n specific_level -p 
```
This initiates the ssh connection

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


