class Button():
    def __init__(self, image, pos, textInput, font, baseColor, hoverColor):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.baseColor = baseColor
        self.hoverColor = hoverColor
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)

    def update(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)
    
    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False
    
    def changeColor(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoverColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)
