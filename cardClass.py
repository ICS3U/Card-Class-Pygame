class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, vals=0):
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])

    def diamond(x, y, width, height, color):
        pygame.draw.polygon(Display, color, ((x, y), (x + width/2, y + height/2), (x, y + height), (x - width/2, y + height/2)))


     
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()

            
#    Card.diamond(100, 0, 100, 150, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))) example run thing            

            import pygame
import random
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
WHITE = (255, 255, 255)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Card:
    # SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    global RANKS
    RANKS = ('Ace','2', '3', '4')

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
          # >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.RANKS[self.rank],
                                   Card.SUITS[self.suit])

    def cardrank():
        rank = random.choice(RANKS)
        pygame.draw.rect(screen, WHITE, [200, 150, 200, 300])
        font = pygame.font.SysFont("comicsansms", 48)  # Setting up the font
        if rank == 'Ace':
            text = font.render("A", True, (0, 0, 0))
            screen.blit(text, (220, 170))  # where to display it
            text1 = font.render("A", True, (0, 0, 0))
            screen.blit(text1, (350, 370))
            pygame.display.flip()
        if rank == '2':
            text = font.render("2", True, (0, 0, 0))
            screen.blit(text, (220, 170))  # where to display it
            text1 = font.render("2", True, (0, 0, 0))
            screen.blit(text1, (350, 370))
            pygame.display.flip()
        if rank == '3':
            text = font.render("3", True, (0, 0, 0))
            screen.blit(text, (220, 170))  # where to display it
            text1 = font.render("3", True, (0, 0, 0))
            screen.blit(text1, (350, 370))
            pygame.display.flip()
        if rank == '4':
            text = font.render("4", True, (0, 0, 0))
            screen.blit(text, (220, 170))  # where to display it
            text1 = font.render("4", True, (0, 0, 0))
            screen.blit(text1, (350, 370))
            pygame.display.flip()

    cardrank()
    while not done:
        # Event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop


if __name__ == '__main__':
    import doctest
    doctest.testmod()
