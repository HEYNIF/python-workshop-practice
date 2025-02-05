import os
import datetime
#command = "uptime"
#command = "date"
'''
def check_cpu(command):  #defining the function
    print(os.system(command))


check_cpu("uptime") #calling the function
 
def check_date(command):
    print(os.system(command))
check_date("date")
'''
'''
def run_command(command):
    return os.system(command)

run_command('uptime')
run_command('df -h')
'''
def showdate():
    return datetime.datetime.today()

today = showdate()
print(today)
