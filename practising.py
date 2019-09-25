import logging
import time
# import os
# from logging.handlers import TimedRotatingFileHandler

class User:

    def parse_param(self):
        """Getting the employee's name and position.
        Here is also main input questions that is addressed to Salesman
        position. if the user types 'Manager' position, he will see the all
        data saved from Salesman employees.
        Also we can see the exceptions handling here, if
        'Manager' or 'Salesman' position is not set by user during
        the input.
        """
        self.name = self._input('name') # this input goes to straight to _imput method with logging
        self.position = self._input('position') # as this

        try:
            if self.position.lower() == 'salesman': # str.lower() - allows us to avoid the issues
                                                    # with capital letters

                # here we can see the file name and 'a' means that the data will be
                # written after the data is already. And the questions are
                salesman_file = open('EmployeeData.txt', 'a')
                q1 = input('Your beverage type: ')
                q2 = input('Any additional ingredients? ')
                q3 = input('The beverage price: ')

                # below formatting is used with global attributes
                data_name = n1 + self.name
                salesman_file.writelines(data_name + n2 + q1 + n2 + q2 + n2 + q3 + n1)
                salesman_file.close()

            # if the user choose 'manager' position to be able to show the summary of all
            # saved data. Here is some logging with global 'logger' parameter
            elif self.position.lower() == 'manager':
                logger.info('Manager is requested the summary of all salesman\'s data')
                time.sleep(0.3) # to have the log first before it prints the data below
                print('you\'re a great manager!')
                f = open('EmployeeData.txt', 'r+')
                s = f.read()
                print('The data entered by your employees are: {}{}'.format(s, n1))
                f.close()

            # if the user is typed position different that 'salesman' or 'manager'
            # the following lines will raise the exception and it's handled above too
            elif self.position.lower() != 'salesman' or 'manager':
                raise Exception('Invalid position!')
        # handling some basic exceptions and logging it as an error
        except (ValueError, TypeError):
            logger.error('type once again')
        except Exception:
            logger.error('Please, type once again')


    def _input(self, var_name):
        """The majority of logging is here.
        The logs are set to be displayed in console on DEBUG level and
        to save in the file log as DEBUG level too.
        However there is a slight difference in formatting to have the
        difference. We can easily set only INFO logs to console and other
        logs(as ERRORs occured by exceptions) go to the file by just changing
        the logging level.
        """
        value = input('Type your {}: '.format(var_name))

        global logger   # in order to log ERROR exception in Exception block
        logger = logging.getLogger(value)   # will take input value to have a name column in logs
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('LogFile.log')    # we will transfer log info to the file
        fh.setLevel(logging.DEBUG)  # we can set the level of logging that goes to the file
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # we could display only INFO logs in console, however I left
                                    # DEBUG logs here
        formatterFH = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatterCH = logging.Formatter('%(name)s - %(levelname)s - %(message)s')   # to differentiate
        ch.setFormatter(formatterCH)
        fh.setFormatter(formatterFH)
        logger.addHandler(ch)
        logger.addHandler(fh)

        logger.info('Entered value: {} as an attribute: {}'.format(value, var_name))
        time.sleep(0.5) # is to have the proper view in the console, where the logs
                        # don't appear out off time and cover the next input message
        return value

class Manager:
    """
    Here we have a formatting method that goes to the file first,
    before initializing parse_param method. Salesman file is
    created here with the heading as Salesman's name; beverage
    type; additional ingredient and its price.
    """
    def file_formatting(self):

        global salesman_file, n1, n2    # these attributes will be used in parse_param method as formatting too
        salesman_file = open('EmployeeData.txt', 'a')   # it is created before initializing parse_param method
                                                        # to have the formatting Heading to the saved data
        n1 = '\n'
        n2 = ' | '
        data_formatting = n1 + 'Salesman\'s name' + n2 + 'Beverage type' + n2 + 'Additional ' \
                                                        'ingredients' + n2 + 'Price' + n1
        salesman_file.writelines(data_formatting)
        salesman_file.close()

def main():
    """
    Main method where we will ask initial question of how many employees
    does the user want to create. It's needed to have the count to repeat
    the method 'parse_param'
    And here we create the objects for both classes and initialize its methods.
    """
    number = int(input('how many employees you will add? '))
    saved_data = Manager()
    saved_data.file_formatting()

    for i in range(number):
        xx = User()
        xx.parse_param()

if __name__ == '__main__':
    main()



# Below is some code to have the logging rotation, however it's not finished yet
# and I hope to have the second chance to be reviewed once again with the following
# additional features:

    # rotation of logs: to create the log file name every day you run the script with
        # the formatting'{}.{}.log' where the suffix is '%Y%m%d'

    # connect the database: SQLite, for instance
    # create unittests
    # to connect listener, multiprocessing: Process, Queue, Event, current_process


    # Rotation

# class Rotation:
#     # def __init__(self, log_directory):
#     #     # global log_directory
#     #     self.log_directory = log_directory
#
#
#     def get_filename(self, filename):
#         # self.filename = filename
#         log_directory = os.path.split(filename)[0]
#
#         date = os.path.splitext(filename)[1][1:]
#
#         filename = os.path.join(log_directory, date)
#
#         if not os.path.exists('{}.log'.format(filename)):
#             return '{}.log'.format(filename)
#
#         index = 0
#         f = '{}.{}.log'.format(filename, index)
#         while os.path.exists(f):
#             index += 1
#             f = '{}.{}.log'.format(filename, index)
#             return f
#
#         rotation_logging_handler = TimedRotatingFileHandler(filename=filename, when='m', ?????????
#                                                             interval=1, backupCount=5)
#         rotation_logging_handler.suffix = '%Y%m%d'
#         rotation_logging_handler.namer =


