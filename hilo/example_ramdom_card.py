import random

card =list(range(1,13))




for i in  range(1,13):
    
   new_card = card.pop(random.randrange(len(card)))
   print(new_card)
   a = input("what is the next h/l: ")
   
   

