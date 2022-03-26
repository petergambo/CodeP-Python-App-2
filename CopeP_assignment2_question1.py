def eqn(userinput):
    minRequirement = 2.5
    F = float(userinput)

    if F < minRequirement:
        return f"FAILED! \nInput is less than {minRequirement}. Try Again.  \n"
    else:
        answer = (F * 10) - 15
        return f" SUCCESS! \n x = ({F} * 10) - 15\n x is {answer} \n"
    
def draw_line(lenType):
    if lenType == "short":
        print("--" * 5)
    elif lenType == "long":
        print("--" * 40)
    else:
        pass

    
#Print Application and Author Information
draw_line("long")
print("NAME: PeterG-1 App              AUTHOR: Peter Aren Gambo (petegambo@gmail.com) \n\nVERSION: 1.0                    DATE: 25th March, 2022\n\nDESCRIPTION: \nThis app solves for x in the equation x = (F * 10) - 15 where F is a user input not less than 2.5. A Code Plateau 3.0 Assignment\n\n")
draw_line("long")

rpt = str("y")

while rpt == "y" or rpt == "Y":
    userinput = float(input("\nTYPE F: "))
    calculatedResult = eqn(userinput)
    print(calculatedResult)
    rpt = str(input("Try Another? Yes(y)/No(n): "))
print("Thank you for using my app! You are awesome \n")
input("press ENTER to exit my app")
