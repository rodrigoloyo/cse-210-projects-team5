# from game.gameOver import  #pending
import random

class Game:
    """The blueprint who directs the game. 
    
    The responsibility of a Game is to control the sequence of play.

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new Game.
        
        Args:
            self (Game): an instance of Game.
        """
        self.card = list(range(1,13))
        self.guess = None
        self.is_playing = True
        self.score = 300
        self.total_score = 0

         
        # game_over = Over()
        # self.card.append(game_over)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing:
            self.display_card()
            self.get_inputs()
            self.display_card()
            # self.do_updates()
            # self.do_outputs()
            self.get_inputs1()
    def display_card(self):

        new_card = self.card.pop(random.randrange(len(self.card)))
        print(new_card)

    def get_inputs(self):
        """Ask the user to guess next card if higher or lower

        Args:
            self (Game): An instance of Game.
            
        """
        guess_card = input("Higher or lower? [h/l]  ")
       

        self.guess = guess_card
        
    def get_inputs1(self):
        new_round = input("Play again? [y/n] ")
        self.is_playing = (new_round == "y")

    