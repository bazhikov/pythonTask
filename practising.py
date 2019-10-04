import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler


class Salesman:
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def process(self):
        action = True
        while action != 'exit':
            action = input('What do you want? \nIf you want to add new sale info, '
                           'please type \'sale\', unless \'exit\' \n')
            if action == 'sale':
                logger.info('{} wants to input the sales info'.format(self.name))
                self.sale_beverage()

            # Add additional available actions if exists with "elif action == 'action_name'"

    def sale_beverage(self):
        salesman_file = open('EmployeeData.txt', 'a')
        q1 = input('Beverage type: ')
        q2 = input('Any additional ingredients? ')
        q3 = input('Beverage price: ')

        # below formatting is used with global attributes
        n1 = '\n'
        n2 = ' | '
        data_name = n1 + self.name
        salesman_file.writelines(data_name + n2 + q1 + n2 + q2 + n2 + q3 + n1)
        salesman_file.close()

        # Save in file

        logger.info('%s sold "%s" beverage for %s', self.name, q1, q3)
        time.sleep(0.5)  # is to have the proper view in the console, where the logs
        # don't appear out off time and cover the next input message

    def file_formatting(self):

        salesman_file = open('EmployeeData.txt', 'a')   # it is created before initializing parse_param method
                                                        # to have the formatting Heading to the saved data
        n1 = '\n'
        n2 = ' | '
        data_formatting = 'Salesman\'s name' + n2 + 'Beverage type' + n2 + 'Additional ' \
                                                        'ingredients' + n2 + 'Price' + n1
        salesman_file.writelines(data_formatting)
        salesman_file.close()


class Manager:
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def process(self):
        action = True
        while action != 'exit':
            action = input('What do you want? \nIf you want to add one more Salesman data '
                           'please type \'salesman\'\nWould like to see all salesman data - '
                           'type \'data\' or do \'exit\' here\n').strip()
            if action == 'salesman':
                client = Salesman(self.name, self.log)
                logger.info('Manager {} wanted to add one more Employee data'.format(self.name))
                time.sleep(0.3)
                client.sale_beverage()

            elif action == 'data':
                logger.info('{} requested all saved employee\'s data displayed'.format(self.name))
                time.sleep(0.3)
                self.saved_data()

    def saved_data(self):
        # Print all salesmen
        f = open('EmployeeData.txt', 'r+')
        s = f.read()
        print('The data entered by your employees are: {}\n\n'.format(s))
        f.close()
        # logger.info('%s requested list of salesmen', self.name)

    # def get_revenue(self):
        # Get revenue

        # logger.info('%s requested revenue amount', self.name)

class Logging:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def logging(self, path):

        global logger  # in order to log ERROR exception in Exception block

        logger = logging.getLogger(self.name)  # will take input value to have a name column in logs
        logger.setLevel(logging.DEBUG)

        fh = TimedRotatingFileHandler(path, when='m', interval=1, backupCount=5)
        fh.prefix = '%Y%m%d'    # can't google anything connecting with prefix, only suffix
                                # that's why I'm afraid it's some pythonic magic, but I liked prefix
                                # more than suffix :)
        fh.setLevel(logging.DEBUG)  # we can set the level of logging that goes to the file
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # we could display only INFO logs in console, however I left
        # DEBUG logs here
        formatterFH = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatterCH = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # to differentiate
        ch.setFormatter(formatterCH)
        fh.setFormatter(formatterFH)
        logger.addHandler(ch)
        logger.addHandler(fh)

        logger.info('Entered value: {} as an attribute: name'.format(self.name))
        time.sleep(0.5)
        # return value



def interactive():

    name = input('What is your name? ')
    role = input('What is your role? ')
    client = None

    log = Logging(name, role)
    log.logging(path='.log')
    logger.info('got the role: {}'.format(role))
    time.sleep(0.5)


    if role.lower() == 'salesman':
        client = Salesman(name, log)
        # client.logging('role')
        client.file_formatting()
    elif role.lower() == 'manager':
        client = Manager(name, log)

    try:
        if client:
            client.process()
        elif self.position.lower() != 'salesman' or 'manager':
            raise Exception('Invalid position!')

    except (ValueError, TypeError):
        logger.error('type once again')
    except Exception:
        logger.error('Invalid position! Please, type once again', interactive())




if __name__ == '__main__':
    interactive()
