import pygame

import constant
from market import Market


class CardUI:

    def __init__(self, card, pos):
        self.card = card
        self.background_color = constant.COLORS.WHITE
        self.title_color = constant.COLORS.BLACK

        self.size = (240, 360)
        self.pos = pos
        self.title = card.name
        self.description = card.description
        self.price = card.price

        self.rect_ui = None

    def draw(self, screen_ref):
        rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.rect_ui = pygame.draw.rect(screen_ref, self.background_color, rect)

        title_label = constant.FONTS.TITLE_FONT.render(self.title, True, self.title_color)
        screen_ref.blit(title_label, self.pos)

        description_label = constant.FONTS.NORMAL_FONT.render(self.description, True, self.title_color)
        screen_ref.blit(description_label, (self.pos[0], self.pos[1] + 50))

    def check_collider(self, point):
        return self.rect_ui.collidepoint(point)

    def click(self):
        market.buy_card(self.card)


pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("MERCADO DE CARTAS")
menuActive = True

pygame.display.flip()

quit_button_size = (150, 40)
quit_button_pos = (0, 25)
quit_button_rect = (quit_button_pos[0], quit_button_pos[1], quit_button_size[0], quit_button_size[1])
quit_button = pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
quit_label = constant.FONTS.NORMAL_FONT.render('Reiniciar Mercado', True, constant.COLORS.WHITE)
screen.blit(quit_label, quit_button_pos)

market = Market()
card_ui_list = []


def draw_market():
    print("drawing market")
    card_ui_list.clear()
    pygame.draw.rect(screen, constant.COLORS.BLACK, (0, 120, 800, 600))
    for i in range(len(market.marketCards)):
        card_ui_item = CardUI(market.marketCards[i], (20 + 260 * i, 120))
        card_ui_item.draw(screen)
        card_ui_list.append(card_ui_item)

    pygame.display.update()


draw_market()

while menuActive:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            menuActive = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if quit_button.collidepoint(mouse_pos):
                market.prepare_market(3)
                draw_market()
            for card_ui in card_ui_list:
                if card_ui.check_collider(mouse_pos):
                    card_ui.click()
                    draw_market()
