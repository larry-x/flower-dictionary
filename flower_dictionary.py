#! /usr/bin/env python3
# Flower_Dictionary: originally a program that allows you to catalog new flower names on an alien planet and save them to a txt file.
# There are just two fields: the first field is limited to 20 characters and the second field is limited to 80 characters.
# It can be used to keep reminders or short diary entries. It can also be used as a phone book.
# However, as this is my first python project the original code to catalog flowers on an alien planet will be kept.

import re, sys, os, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.info('Welcome to the program.')

book = {}
flower_path = None
planet_name = None

def entry_prompt():
    
    global flower_path
    global planet_name
    while True:
        print('What planet are you updating the flower log for? (File name please)')
        dr_name = os.getcwd()
        planet_name = input()
        flower_path = os.path.join(dr_name, planet_name + '.txt')
        if planet_name and os.path.exists(flower_path):
            validity()
        else:
            new_file()

def new_file():

    while True:
        print('The file for planet "%s" does not exist. Create new file?' % planet_name)
        answer = input()
        if planet_name and answer.lower() == 'yes':
            new_file = open(flower_path, 'w')
            new_file.write('This is a flower log for planet %s.'.center(150) % planet_name + '\n\n')
            new_file.close()
            validity()
        elif answer.lower() == 'no':
            entry_prompt()
        else:
            print('Please type "yes" or "no".')
            continue
        
def validity():

    while True:
        print('Please name this new flower. You can use letters and numbers, but cannot start with a number.')
        trythis = input()
        trythis_reg = re.compile(r'^[a-zA-Z][a-zA-Z0-9]+$')
        trythis_match = trythis_reg.search(trythis)
        if trythis_match == None:
            print('Sorry, no special characters or spaces allowed, and start with a letter. \n')
            continue
        elif len(trythis) < 3 or len(trythis) > 15:
            print('Sorry, the name must be at least 3 characters, but no more than 15 characters.')
            continue
        else:
            print('Lovely. Now let\'s have a quick description of this flower. Please be brief.')
            trythat = input()
            while len(trythat) == 0 or len(trythat) > 80:
                print('Your description must not exceed 80 characters but must be at least one character.')
                trythat = input()
        book.update({trythis : trythat})
        addanother()

def addanother():

    print('Do you have more entries to make? Answer "yes" or "no".')
    answer = input()
    if answer.lower() == 'yes':
        validity()
    elif answer.lower() == 'no':
        edit_file()
    else:
        addanother()
               
def edit_file():
    
    global flower_path
    c_file = open(flower_path, 'a')
    for n, d in book.items():
        c_file.write('{:30s} :: {} \n'.format(n, d))
    c_file.close()
    content = open(flower_path, 'r')
    print(content.read())
    content.close()
    sys.exit()

entry_prompt()
