import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler
import unittest
import argparse


class Salesman:
    """
    Class for Salesman role.
    Here we have common method 'process' that gives an option to select
    between two actions: 'sale' or 'exit'.
    'Sale' action gives an opportunity to input sale data and save it
    into the file.
    """
    def __init__(self, name, log):
        """
        Name and log attributes are set here to have them in our
        methods. Refer to main() function to find 'log' object of
        Logging class.
        """
        self.name = name
        self.log = log


    def process(self):
        """
        The cycle is applied while the action is not 'exit'. So the user can type
        'exit' to be exited. The additional actions can be added here.
        """

        action = True
        while action != 'exit':
            action = input('What do you want to do? \nIf you want to add new sale info, '
                           'please type \'sale\', unless do \'exit\' here \n')
            if action == 'sale':
                logger.info('{} wants to input the sales info'.format(self.name))
                time.sleep(0.3)
                self.sale_beverage()
            elif action == 'exit':
                logger.info('Salesman {} is exited the program'.format(self.name))
            else:
                logger.error('Salesman {} typed \'{}\' as an action, that is not valid!'.format(self.name, action))
                print('Please choose the appropriate action')

            # Add additional available actions if exists with "elif action == 'action_name'"

    def sale_beverage(self):
        """
        The file is created here with the mode: 'a' that means that the new data
        placed by another user won't be override previous data, it will be
        placed after.
        """
        salesman_file = open('EmployeeData.txt', 'a')
        q1 = input('Beverage type: ')
        q2 = input('Any additional ingredients? ')
        q3 = input('Beverage price: ')

        n1 = '\n'
        n2 = ' | '
        data_name = n1 + self.name
        salesman_file.writelines(data_name + n2 + q1 + n2 + q2 + n2 + q3 + n1)
        salesman_file.close()


        logger.info('%s sold "%s" beverage for %s', self.name, q1, q3)
        time.sleep(0.5)  # is to have the proper view in the console, where the logs
        # don't appear out off time and cover the next input message

    def file_formatting():
        """
        Thus there is no table created in some DB, the simple(monkey) formatting is
        configured here.
        """
        n1 = '\n'
        n2 = ' | '
        salesman_file = open('EmployeeData.txt', 'a')
        data_formatting = '\nSalesman\'s name' + n2 + 'Beverage type' + n2 + 'Additional ' \
                                                                           'ingredients' + n2 + 'Price' + n1
        salesman_file.writelines(data_formatting)
        salesman_file.close()

class Manager:
    """
    Class for Managers. It has also common method "process", but with its own
    unique actions. Manager is able to load the saved data of all employees added,
    furthermore, there is an additional opportunity added for manager is to be
    able to input one more additional salesman data instead of salesman.
    Cause managers can do the salesman job when it's needed or all the salesmans
    are busy and etc.
    """
    def __init__(self, name, log):
        """same name and log attributes and initialized here"""
        self.name = name
        self.log = log

    def process(self):
        """
        Managers have the option between inputting the additional salesman data;
        loading the saved data from the file and to exit the program.
        """
        action = True
        while action != 'exit':
            action = input('What do you want to do? \nIf you want to add one more Salesman data '
                           'please type \'salesman\'\nWould like to see all salesman data - '
                           'type \'data\' or do \'exit\' here\n')
            if action == 'salesman':
                client = Salesman(self.name, self.log)
                logger.info('Manager {} wanted to add one more Employee data'.format(self.name))
                time.sleep(0.3)
                client.sale_beverage()

            elif action == 'data':
                logger.info('{} requested all saved employee\'s data displayed'.format(self.name))
                time.sleep(0.3)
                self.saved_data()
            elif action == 'exit':
                logger.info('Salesman {} is exited the program'.format(self.name))
            else:
                logger.error('Manager {}\'s chosen \'{}\' as an action, that is not valid!'.format(self.name, action))
                print('Please choose the appropriate action')

    def saved_data(self):
        """Print all salesman' data"""
        f = open('EmployeeData.txt', 'r+')
        s = f.read()
        print('The data entered by your employees are: {}\n\n'.format(s))
        f.close()

class Logging:
    """
    Class for logging and its rotation handler. There are 2 handlers that are:
    StreamHandler that lets us to have the INFO logs in the console itself and
    Rotation file handler that is saved into the '.log' file. After the second
    script run, the previous '.log' file will be renamed with the formatting
    as '.log.YYYY-MM-DD_hh-mm' and it has backUp=5, that means that the sixth
    log file will be deleted automatically after the 7th script run.
    """
    def __init__(self, name):
        """
        Name attribute is initialized here to have it as a logger name.
        So the user name will be displated in the logs.
        """
        self.name = name

    def logging(self, path):
        """
        The logging settings. We have global 'logger' here to be able to log
        every operation in this program.
        """
        global logger

        logger = logging.getLogger(self.name)  # will take input value to have a name column in logs
        logger.setLevel(logging.DEBUG)

        fh = TimedRotatingFileHandler(path, when='m', interval=1, backupCount=5)
        fh.prefix = '%Y%m%d'    # can't google anything connecting with prefix, only suffix
                                # that's why I'm afraid it's some pythonic magic, but I liked prefix
                                # more than suffix :)
        fh.setLevel(logging.DEBUG)  # we can set the level of logging that goes to the file
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatterFH = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatterCH = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # to differentiate
        ch.setFormatter(formatterCH)
        fh.setFormatter(formatterFH)
        logger.addHandler(ch)
        logger.addHandler(fh)


def commandline():
    """
    Function for commandline interface. As you can see from the below, there is
    an option to set name and role arguments prior the script run.
    """
    parser = argparse.ArgumentParser(description='You can type your name and role')
    parser.add_argument('-n', '--name', type=str, help='user\'s name')
    parser.add_argument('-r', '--role', type=str, help='user\'s role')
    args = parser.parse_args()

    if args.name is None:
        interactive()
    else:
        main(args.name, args.role)



def interactive():
    """
    The function is for interactive interface that gets the main input if the args
    are ignored in CLI during the script run.
    """
    name = input('What is your name? ')
    role = input('What is your role? ')

    main(name, role)


def main(name, role):
    """
    Main function in this program with the 'name' and 'role' attributes.
    All objects are in this method and the Classes are initialiazed here too.
    Also some Exceptions and errors handling applied here.
    The log file name is defined here with the path variable.
    """
    client = None

    log = Logging(name)
    log.logging(path='.log')
    logger.info('Entered value: {} as an attribute: name'.format(name))
    logger.info('got the role: {}'.format(role))
    time.sleep(0.5)

    file_formatting() # refer to the function below

    if role.lower() == 'salesman':
        client = Salesman(name, log)
        client.file_formatting()
    elif role.lower() == 'manager':
        client = Manager(name, log)

    try:
        if client:
            client.process()
        elif role.lower() != 'salesman' or 'manager':
            raise Exception('Invalid position!')
    except (ValueError, TypeError, Exception):
        print('Invalid position! Please, type once again')

if __name__ == '__main__':
    commandline()
