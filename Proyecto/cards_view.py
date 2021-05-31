import pygame

import constant
from market import Market


class CardUI:

    def __init__(self, card, pos):
        self.card = card
        self.background_color = constant.COLORS.WHITE
        self.background_color_description = constant.COLORS.GRAY75
        self.title_color = constant.COLORS.BLACK

        self.size = (240, 360)
        self.pos = pos
        self.title = card.name
        self.description = card.description
        self.price = card.price

        self.rect_ui = None

    def draw(self, screen_ref):
        rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        rectTitle = (self.pos[0]+20, self.pos[1]+50, self.size[0], self.size[1]-20)
        rectDescription = (self.pos[0]+20, self.pos[1]+120, self.size[0]-40, self.size[1]-140)
        marginContainer = 5
        rectDescriptionContainer = (rectDescription[0] - marginContainer, rectDescription[1] - marginContainer,
                                    rectDescription[2] + marginContainer*2, rectDescription[3] + marginContainer*2)
        rectPrice = (self.pos[0]+100, self.pos[1]+10, self.size[0], self.size[1])

        self.rect_ui = pygame.draw.rect(screen_ref, self.background_color, rect, border_radius=10)
        self.rect_ui = pygame.draw.rect(screen_ref, self.background_color_description, rectDescriptionContainer,
                                        border_radius=marginContainer)

        #title_label = constant.FONTS.TITLE_FONT.render(self.title, True, self.title_color)
        #screen_ref.blit(title_label, self.pos)
        drawText(screen_ref, self.title, constant.COLORS.BLACK, rectTitle, constant.FONTS.TITLE_FONT)

        #description_label = constant.FONTS.NORMAL_FONT.render(self.description, True, self.title_color)
        #screen_ref.blit(description_label, (self.pos[0], self.pos[1] + 50))

        drawText(screen_ref, self.description, constant.COLORS.BLACK, rectDescription, constant.FONTS.NORMAL_FONT)
        drawText(screen_ref, str(self.price), constant.COLORS.GREEN, rectPrice, constant.FONTS.SUBTITLE_FONT)

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


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=True, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


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




