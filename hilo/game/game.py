import random


class Game:
    """A person who directs the game. 

    The responsibility of a Game is to control the sequence of play. """

    

    def __init__(self):
        """Constructs a new Game.

        Args:
            self (Game): an instance of Game.
        """
        self.card = list(range(1, 13))
        self.current_card = 0
        self.new_card = 0
        
        self.guess = 0
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        # die = Die()
        # self.card.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing or self.score == 0 :
            self.display_card()
            self.get_inputs()        
            self.do_updates()
            self.do_outputs()
            self.get_inputs1()

     

    def get_inputs(self):
        """Ask the user  for higher or lower choice.

        Args:
            self (Game): An instance of Game.

        """
        print("this is the current card")
        print(self.current_card)
       
        guess_card = input("Higher or lower? [h/l]  ")

        self.guess = guess_card
       

    def display_card(self):

        self.new_card = self.card.pop(random.randrange(len(self.card)))
        
           

    def get_inputs1(self):
    
       
        new_round = input("Play again [y/n] ")
        self.is_playing = (new_round == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Game): An instance of Game.
        """
        print("this is the new  card")
        print(self.new_card)
        if self.new_card > self.current_card:
            if  self.guess == "h":
                self.score += 100
            else: 
                 self.score -= 100
        if self.new_card < self.current_card:
            if  self.guess == "l":
                self.score += 100

            else: 
                 self.score -= 100
            
           

        self.current_card = self.new_card
        

    def do_outputs(self):
        """Displays  the score. Also asks the player if they want to play again. 

        Args:
            self (Game): An instance of Game.
        """
        if not self.is_playing:
            return

        
        print(f"Your score is: {self.score}\n")
        self.is_playing == (self.score > 0)
