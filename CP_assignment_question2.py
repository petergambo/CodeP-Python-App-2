import re                                                                           #I import the Python re module to use its split() method later

def set_attribute(text):                                                            #custom function to set proper attributes for text (str) and number (int)
    return int(text) if text.isdigit() else text

def natural_keys(text):                                                             #this method will sort our list of numbers in a natural way i.e 1,2,3,30,100,203 and not the default 1,100,2,203,3,30
    return [set_attribute(c) for c in re.split(r'(\d+)', text)]

def draw_line(lenType):                                                             #this custom method will draw a line separator on the output screen. The line is either short or long
    if lenType == "short":
        print("--" * 5)
    elif lenType == "long":
        print("--" * 40)
    else:
        pass                                                                        #do nothing

#Print Application and Author Information
draw_line("long")
print("NAME: PeterG-2 App\nVERSION: 0.0.0\nDESCRIPTION: Analyses and get's the highest number in a list of numbers. A Code Plateau 3.0 Assignment\nCREATOR: Peter Aren Gambo (petegambo@gmail.com)\nDATE: 25th March, 2022")
draw_line("long")

#Create some Variables that I will need later
items = []                                                                          #creates an empty list and store in a variable named items. This would later hold the user inputed data for our analysis
cur_index = 1                                                                       #set a variable named cur_index to 1. This would be used to count the number of data the user is inputing to our items list
total_item_number = int(input("HOW MANY ITEMS DO YOU WANT TO ANALYZE? \n(Should be Greater than 5 and Less than 7): \n"))      #Allow users to specify the number of items they want to add to our items list


if (total_item_number < 5 or total_item_number > 7):                                #check if item number fails the reqired condition
    print("Oops!!! \nItems should be greater than 5 and less than 7! Run app again")#then terminate with this message and draw a long line below it
    draw_line("long")    
else:
    print("Great!")                                                                 #But if condition is passed, allow user add the number of items they specified in total_item_number above using a loop
    for item in range(total_item_number):                                           #the loop condition
        item = input(f"TYPE ITEM {cur_index} of {total_item_number}:  ")            #get the item from user input. Show the user serial number of each item they are adding
        items.append(item)                                                          #Add the item to our item list
        cur_index = cur_index + 1                                                   #update item serial number that would be displayed for the next item. Simply add 1 to the current serial number to generate the next.
    draw_line("short")                                                              #draw a short line after we have received all the specified number of items from the loop
    unsorted = str(items)                                                           #save a new copy of the item list before I sort the original list. I want to display the unsorted list to the user later

    print(f"Great!\nThe list {unsorted} has been generated Successfully!")          #Display to the user the list that was generated successfully
    
    items.sort(key=natural_keys, reverse=True)                                      #Next to get the highest value from our list, I sort the list in a natural order. Descending the sort order makes the Highest value to start at index 0
    highest = items[0]                                                              #Now I can picked the first value from our sorted list as the Highest and store it in the variable called "highest"
    print(f"The highest number in the list is {highest}")                           #output result to user
    draw_line("long")                                                               #draw a line to specify end of code

input("Press ENTER to exit my app")
