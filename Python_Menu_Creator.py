#Date: 1/5/2022
#Author: Joshua W Smith (github.com/jws8)

#Menu Creator and Random Menu Item Generator: prompts user for additional items
#Upon app close returns a random menu item 
import random
#create list for menu items
class Python_Menu_Creator():
    def __init__ (self):
        self.rans_list = []
        self.menu_items = []
        self.message = ""

    #read_file() splits entire text contents into a list seperated by commas
    # and appends that list to menu_items list
    def read_file(self, file_location):
        with open(file_location) as f:
            for line in f:
                self.menu_items.append(line.split(","))
    def generate_week(self):
        week_dict = {"Monday": "", "Tuesday": "", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday":"", "Sunday": ""}
        week_list = list(week_dict.keys())
        print(week_list)
        count = 0
        i = 1
        for i in range(7):
            rans = random.choice(self.menu_items[0])
            while rans in week_dict.values():
                    count+=1
                    rans = random.choice(self.menu_items[0])
            else:  
                week_dict[str(week_list[i])] = rans
                self.message = self.message + "\n" + str(week_list[i] + " " + week_dict[str(week_list[i])].title())
        print(count)
        print(self.message)
    #prompts user for new item, updates menu item list and text file.
    #generates random menu item upon close
    def prompt(self):  
        while True:
            ans = input("item: ")
            if ans == "":
                #generate random choice out of menu items 
                #& exit prompt loop
                rans = random.choice(self.menu_items[0])
                self.rans_list.append(rans)
                print(rans)
                break #gotta get outta here
            #update file with new item
            self.write_file(ans)
            #update menu items with new item
            self.menu_items.append(ans)
    #writes new item (ans) to text file
    def write_file(self,ans):
        with open("menu_items.txt", "a") as f:
                f.write(ans + ",")


#Run Template
#PMC = Python_Menu_Creator()
#PMC.read_file("menu_items.txt")
#PMC.prompt()
#PMC.generate_week()
#print(PMC.message)




        