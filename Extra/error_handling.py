import sys
import time
import traceback


def excepter(message):  #  message from the telegram bot or ''
    error_class = sys.exc_info()[0]
    error = sys.exc_info()[1]
    line = sys.exc_info()[2].tb_lineno
    
    mas_time = time.asctime().split()
    string_time = mas_time[2] + " " + mas_time[1] + " " + mas_time[4] + " | " + mas_time[3]
    
    file_name = "Error"
    file = open('{0}.txt'.format(file_name), 'w')
    file.write('Filename: ' + 'Main bot file' + '\n')
    file.write('Line: ' + str(line) + '\n')
    file.write('Error class: ' + str(error_class) + '\n')
    file.write('Error: ' + str(error) + '\n')
    file.write('Time: ' + str(string_time) + '\n')
    file.write('\n')
    if message == '':
        file.write('User:' + '\n')
        file.write('No information' + '\n')
        file.write('Can extract information from telegram message' + '\n')
        file.write('\n')
    else:
        file.write('USER:' + '\n')
        file.write('id: ' + str(message.from_user.id) + '\n')
        file.write('is_bot: ' + str(message.from_user.is_bot) + '\n')
        file.write('username: ' + str(message.from_user.username) + '\n')
        file.write('first_name: ' + str(message.from_user.first_name) + '\n')
        file.write('last_name: ' + str(message.from_user.last_name) + '\n')
        file.write('language_code: ' + str(message.from_user.language_code) + '\n')
        file.write('\n')
    file.write('System traceback:' + '\n')
    for sys_string in traceback.format_tb(sys.exc_info()[2]):
        file.write(str(sys_string))
    file.close()
    
    '''
    file_to_send = open('{0}.txt'.format(file_name), 'r')
    bot.send_document(287352001, file_to_send)
    '''


try:
    1/0
except:
    excepter('')


'''

sys.exc_info() = 
0) <class 'ZeroDivisionError'>             Type
1) ZeroDivisionError('division by zero',)  Value
2) <traceback object at 0x04817800>        Traceback

exc_type, exc_value, exc_traceback = sys.exc_info()

print('1 print_tb')
traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
print()

print('2 print_exception')
traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
print()

print('3 print_exc')
traceback.print_exc()
print()

print('4 format_exc')
formatted_lines = traceback.format_exc().splitlines()
print(formatted_lines[0])
print(formatted_lines[-1])
print()

print('5 format_exception')
print(traceback.format_exception(exc_type, exc_value, exc_traceback))
print()

print('6 extract_tb')
print(traceback.extract_tb(exc_traceback))
print()

print('8 format_tb')
print(traceback.format_tb(exc_traceback))
print()

print('9 TracebackException')
print(type(traceback.TracebackException.from_exception(e)))
print(traceback.TracebackException.from_exception(e))
print()

'''