w_bank = []
fname = "christian kyle"
ask_usr = ""
while True:
    if ask_usr.lower() == fname or ask_usr.lower() == "":
        word = str(input("Enter the word: "))
    elif ask_usr.lower() == "autor":
        break     
    else:
        print("Invalid input!", "Please try again.", sep="\n")
       
    ask_usr = str(input("Do you want to append more word? if yes input 'christian kyle' otherwise input 'autor': "))
    if ask_usr.lower() == fname:
        w_bank.append(word)
                
print("Word Bank", w_bank)      
 
 
