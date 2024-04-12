fname = ""
lname = ""
def storeWords():
    w_bank = []
    ask_usr = ""
    while True:
        if ask_usr.lower() == fname or ask_usr.lower() == "":
            word = str(input("Enter the word: "))
        elif ask_usr.lower() == lname:
            break     
        else:
            print("Invalid input!", "Please try again.", sep="\n")
        
        ask_usr = str(input(f"Do you want to append more word? if yes input '{fname}' otherwise input '{lname}': "))
        if ask_usr.lower() == fname:
            w_bank.append(word)
    print("Word Bank", w_bank)

def setFirstName(_fname):
    global fname
    fname = _fname.lower()

def setLastName(_lname):
    global lname
    lname = _lname.lower()
