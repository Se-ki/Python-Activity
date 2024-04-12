"""
    Pasaol is equal to Rock 
    Arnel is equal to Paper
    Aicy is equal to Scissors 
    Jodelyn is equal to Lizard
    Kyle is equal to Spock
"""
import random
print(__doc__, "This is the Pasaol-Arnel-Aicy-Jodelyn-Kyle Game", sep="\n", end="\n")
chos = ["pasaol","arnel","aicy","jodelyn","kyle"]    

p1 = input("Player 1: ") 
p2 = random.choice(chos)
print("Player 2:", p2)


if p1.lower() == "aicy" and p2.lower() == "arnel":
    print("Aicy cuts Arnel", "Winner p1", sep="\n")
elif p2.lower() == "aicy" and p1.lower() == "arnel":    
    print("Aicy cuts Arnel", "Winner p2", sep="\n")
elif p1.lower() == "arnel" and p2.lower() == "pasaol":    
    print("Arnel covers Pasaol", "Winner p1", sep="\n")
elif p2.lower() == "arnel" and p1.lower() == "pasaol":    
    print("Arnel covers Pasaol", "Winner p2", sep="\n")
elif p1.lower() == "pasaol" and p2.lower() == "jodelyn":  
    print("Pasaol crushes Jodelyn", "Winner p1", sep="\n")  
elif p2.lower() == "pasaol" and p1.lower() == "jodelyn":    
    print("Pasaol crushes Jodelyn", "Winner p2", sep="\n")  
elif p1.lower() == "jodelyn" and p2.lower() == "kyle":  
    print("Jodelyn poisons Kyle", "Winner p1", sep="\n")  
elif p2.lower() == "jodelyn" and p1.lower() == "kyle":    
    print("Jodelyn poisons Kyle", "Winner p2", sep="\n")  
elif p1.lower() == "kyle" and p2.lower() == "aicy":  
    print("Kyle smashes Aicy", "Winner p1", sep="\n")  
elif p2.lower() == "kyle" and p1.lower() == "aicy":    
    print("Kyle smashes Aicy", "Winner p2", sep="\n") 
elif p1.lower() == "aicy" and p2.lower() == "jodelyn":  
    print("Aicy decapitates Jodelyn", "Winner p1", sep="\n")  
elif p2.lower() == "aicy" and p1.lower() == "jodelyn":    
    print("Aicy decapitates Jodelyn", "Winner p2", sep="\n")
elif p1.lower() == "jodelyn" and p2.lower() == "arnel":  
    print("Jodelyn eats Arnel", "Winner p1", sep="\n")  
elif p2.lower() == "jodelyn" and p1.lower() == "arnel":    
    print("Jodelyn eats Arnel", "Winner p2", sep="\n")    
elif p1.lower() == "arnel" and p2.lower() == "kyle":  
    print("Arnel disproves Kyle", "Winner p1", sep="\n")  
elif p2.lower() == "arnel" and p1.lower() == "kyle":    
    print("Arnel disproves Kyle", "Winner p2", sep="\n")   
elif p1.lower() == "kyle" and p2.lower() == "pasaol":  
    print("Kyle vaporizes Pasaol", "Winner p1", sep="\n")  
elif p2.lower() == "kyle" and p1.lower() == "pasaol":    
    print("Kyle vaporizes Pasaol", "Winner p2", sep="\n")      
elif p1.lower() == "pasaol" and p2.lower() == "aicy":  
    print("Pasaol vaporizes Aicy", "Winner p1", sep="\n")  
elif p2.lower() == "pasaol" and p1.lower() == "aicy":    
    print("Pasaol vaporizes Aicy", "Winner p2", sep="\n")                    
elif p1.lower() == p2.lower():
    print("Tie!")    
else:
    print("Invald input you must input like Pasaol, Arnel, Aicy, Jodelyn or Kyle")    


