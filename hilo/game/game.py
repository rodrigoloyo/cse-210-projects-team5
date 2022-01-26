import random


class Game:
    """A person who directs the game. 
    
    The responsibility of a Game is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Game.
        
        Args:
            self (Game): an instance of Game.
        """
        self.card = list(range(1,13))
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
        while self.is_playing:
            self.display_card()
            self.get_inputs()
            self.display_card()
            self.do_updates()
            self.do_outputs()
            self.get_inputs1()

    def display_card(self):

        new_card = int(self.card.pop(random.randrange(len(self.card))))
        return new_card
        

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Game): An instance of Game.
            
        """
        guess_card = input("Higher or lower? [h/l]  ")
       

        self.guess = guess_card
        print(self.guess)
    def display_card(self):

        self.current_card = self.card.pop(random.randrange(len(self.card)))
        print(self.current_card)
        print(type(self.new_card))

    

    def get_inputs1(self):
        new_round = input("Play again [y/n] ")
        self.is_playing = (new_round == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Game): An instance of Game.
        """
        # if not self.is_playing:
        #     return 

        # for i in range(len(self.dice)):
        #     die = self.dice[i]
        #     die.roll()
        #     self.score += die.points 
        # self.total_score += self.score
        print(type(self.card))
         
        new_card = self.display_card()
        print(type(self.current_card))
        print("test")
        print(type(new_card))
        # print(type(self.new_card, type(self.current_card)))

        if self.new_card > self.current_card and self.guess == "h":

          self.score += 100
        else:
            self.score -= 100
        print(self.score)

     



    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Game): An instance of Game.
        """
        if not self.is_playing:
            return
        
        # values = ""
        # for i in range(len(self.dice)):
        #     die = self.dice[i]
        #     values += f"{die.value} "

        # print(f"You rolled: {values}")
        print(f"Your score is: {self.score}\n")
        self.is_playing == (self.score > 0)