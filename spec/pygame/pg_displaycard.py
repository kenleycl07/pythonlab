##########
### pygame
### display a card
##################

# Display the image of a card.
def display_card():

    pygame.init()

    WIDTH = 300
    HEIGHT = 250
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    card = pygame.image.load("images/cT.jpg")
    card.convert()
    card_size = card.get_rect()

    condition = True
    while condition:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condition = False

        screen.blit(card, card_size)
        pygame.display.update()

display_card()





