# from game.gameOver import  #pending


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

         
        # die = Die()
        # self.card.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing:
            self.get_inputs()
            # self.do_updates()
            # self.do_outputs()
            self.get_inputs1()

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

    