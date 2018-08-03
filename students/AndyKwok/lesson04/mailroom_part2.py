# Description: Mailroom Program (Database Organizer)
# Author: Andy Kwok
# Last Updated: 07/23/2018
# ChangeLog: 
# v1.0 - Initialization
# v2.0 - Adopt file creation and dictionary types

#!/usr/bin/env python3

if __name__ == '__main__':    
    database = {'Donor A': [2300.30, 1000.01, 2000.00],
                'Donor B': [1394.12],
                'Donor C': [14349.00, 175.95],
                'Donor D': [42800.11, 1500.04, 3534.20],
                'Donor E': [12312.23, 250.50]}
    
def thank_you_select(database):
    """ Function
    """
    entry = input('Enter donor\'s name to search or \'list\' to show all donors> ')
    if entry == 'list':
        database_print(database)
    else:
        database = add_donation(entry, database)

def report_select(database):
    """ Function to sort the database and printout the sorted database
    """
    database = dict(sorted(database.items(), key=lambda x: x[1], reverse=True))
    database_print(database)

def letters_everyone(database):
    for k, v in database.items():
        file = open(k.replace(" ", "_") + ".txt", "w")
        file.write(send_thank_you(k, v))
    
def add_donation(name, database):
    """ Function to add new donation to the database
    """
    donation = float(input('How much does {} want to donate? '.format(name)))
    if database.get(name) is not None:
        database[name] += [donation]
    else:
        database.update({name: [donation]})
    print(send_thank_you(name, [donation]))
    

def database_print(database):
    """ Function to display donor's information in a table format
    """
    print('Donor Name' + ' '*10 + '| Total Given' + ' '*5 + '| Num Gifts' + ' '*5 + '| Average Gift')
    print('-'*75)
    for donor, donation in database.items():
        print('{:20} '.format(donor) + '$ {:>10.2f} {:7}'.format(sum(donation), len(donation)) + ' '*14 + '$ {:>10.2f}'.format(sum(donation)/len(donation)))
        
def send_thank_you(name, donation):
    """ Function that prints input into formated string
    """
    printout = 'To {},'.format(name) + '\n' + 'Thank you for your donation of ${:.2f}.'.format(sum(donation)) + '\n'*2 + '\t'*5 + '-System Generated Email'
    return printout

def quit_select(database):
    """ Function to trigger the program to exit
    """
    global option
    option = 'quit'

option = 'start'
menu = {'1': thank_you_select, '2': report_select, '3': letters_everyone, '4': quit_select}

while option.lower() != 'quit':
    print(
        '''    
        1 - Sent a Thank you
        2 - Create a Report
        3 - Send Letters to Everyone
        4 - Quit
        '''
        )
    option = input('Please select an option> ')
    menu[option](database)
