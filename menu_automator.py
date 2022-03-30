from Python_Menu_Creator import *
from MailSight import *
import time
#set current time to now
now = time.time()
PMC = Python_Menu_Creator()
my_gmail = MailSight()
#NEED TO AUTOMATE THIS USING OS AND ENVIRON VARS IN ANOTHER EXECUTABLE
#this is a run template, need to hard write in the string for automation examples given
my_gmail.set_username_password("YourEmail@gmail.com", "YourPassword")
#this list needs to be hard written in as well for automation, but you can write a method to input an email list in
email_list = ["Mom@gmail.com", "Dad@outlook.com", "Spouse@hotmail.com"]
#if you wish to add items to the list add PMC.prompt()
#read list of menu items from a text file
#PMC.read_file("C:\\Users\\jarch_dvn5pc0\\OneDrive\\Desktop\\Programming_Python\\automation\\automators\\MenuAutomator\\menu_items.txt")
PMC.read_file("file_path")
#generate "week formatted" list by the read file
PMC.generate_week()

#send email from MailSight object
my_gmail.send_mail("This is a message from the Menu Generator app for the week of " + str(time.ctime(now)), PMC.message, email_list)

 