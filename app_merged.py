import re                                                                           #I import the Python re module to use its split() method later

def natural_keys(text):                                                             #this method will sort our list of numbers in a natural way i.e 1,2,3,30,100,203 and not the default 1,100,2,203,3,30
    return float(text)

def eqn(userinput):
    minRequirement = 2.5
    F = float(userinput)
    if F < minRequirement:
        return False
    else:
        x = (F * 10) - 15
        return x

def draw_line(lenType):                                                             #this custom method will draw a line separator on the output screen. The line is either short or long
    if lenType == "short":
        print("--" * 5)
    elif lenType == "long":
        print("--" * 40)
    else:
        pass                                                                        #do nothing



#Print Application and Author Information
draw_line("long")
print("NAME: PeterG-2 App                                       VERSION: 0.0.0\nCREATOR: Peter Aren Gambo (petegambo@gmail.com)          DATE: 25th March, 2022 \nDESCRIPTION: Analyses and get's the highest number in a list of numbers. A Code Plateau 3.0 Assignment\n")
draw_line("long")

#Create some Variables that I will need later

running = 1                                                                     #creates a variable "running" and sets it to 1. We will use this value to make my code restart after completion

while running == 1:                                                             #make our code loop or repeat as long as variable running remains 1
    items = []                                                                      #First creates an empty list called items. This would later hold the user inputed data for our analysis
    serial_no = 1                                                                   #set a variable "serial_no" to 1. This would be used to show serial number for each user input to our items list

    while len(items) < 7:                                                           #allows user to keep adding variables as long as total item in list is less than 7
        item = str(input(f">>> TYPE ITEM {serial_no}:  "))
        
        if(eqn(item) == False):                                                     #if eqn() returns false, then the user input is less than 2.5. 
            print(f"FAILED! Input is less than 2.5. Try Again.")                    #Return this error
        else:
            calculatedResult = eqn(item)                                            #if eqn() is not false, then get the solved result i.e x = (F * 10) - 15
            items.append(calculatedResult)                                          #add the result to our items list
            serial_no = serial_no + 1                                               #set the next item serial number by updating present serial_no with + 1
            print(f"{items} - {len(items)} items")                                  #show the user the new list and display the number of items in it
            
    items.sort(key=natural_keys, reverse=True)                                      #Next to get the highest value from our list, I first sort the list in a natural order. then descend the sort order so that the Highest value becomes first in the list
    highest = items[0]                                                              #Now, I get the first value from the sorted list with items[0] and store it in a variable called "highest"
    print(f"The highest number in the list is {highest}")                           #At this point, Process Complete! Next I Display the highest number in the list to user
    draw_line("long")                                                               #draw a line to specify end of code

    tryAgain = input("Try Another? Y/N: ")
    print('\n')
    if tryAgain == 'y' or tryAgain == 'Y' or tryAgain == 'yes' or tryAgain == 'Yes'or tryAgain == 'YES':
        running = 1
    elif tryAgain == 'n' or tryAgain == 'N' or tryAgain == 'no' or tryAgain == 'No' or tryAgain == 'NO':
        running = 0

input("Press ENTER to exit Peter's App")
