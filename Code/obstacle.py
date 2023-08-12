import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))


shape = [
    '                    xxxxxxxxxxxxxxxxxxx                   `',
    '                 xxxxxx             xxxxxxx                ',
    '              xxxx                       xxxx              ',
    '             xxx                             xx            ',
    '            xx                                xx           ',
    '           xx                     `           xx          `',
    '          xx                                   xx          ',
    '          xx xx                             xx xx          ',
    '          xx xx                             xx  x          ',
    '          xx xx                             xx  x          ',
    '          xx  xx                            xx xx          ',
    '          xx  xx                           xx  xx          ',
    '           xx xx   xxxxxxxx     xxxxxxxx   xx xx           ',
    '            xxxx xxxxxxxxxx     xxxxxxxxxx xxxxx           ',
    '             xxx xxxxxxxxxx     xxxxxxxxxx xxx             ',
    '    xxx       xx  xxxxxxxx       xxxxxxxxx  xx      xxxx   ',
    '   xxxxx     xx   xxxxxxx   xxx   xxxxxxx   xx     xxxxxx  ',
    '  xx   xx    xx     xxx    xxxxx    xxx     xx    xx   xx  ',
    ' xxx    xxxx  xx          xxxxxxx          xx  xxxx    xxx ',
    'xx         xxxxxxxx       xxxxxxx       xxxxxxxxx        xx',
    'xxxxxxxxx     xxxxxxxx    xxxxxxx    xxxxxxxx      xxxxxxxx',
    '  xxxx xxxxx      xxxxx              xxx xx     xxxxxx xxx ',
    '          xxxxxx  xxx  xx           xx  xxx  xxxxxx        ',
    '              xxxxxx xx xxxxxxxxxxx xx xxxxxx              ',
    '                  xx xx x x x x x x x x xx                 ',
    '                xxxx  x x x x x x x x   xxxxx              ',
    '            xxxxx xx   xxxxxxxxxxxxx   xx xxxxx            ',
    '    xxxxxxxxxx     xx                 xx      xxxxxxxxx    ',
    '   xx           xxxxxxx             xxxxxxxx          xx   ',
    '    xxx     xxxxx     xxxxxxxxxxxxxxx     xxxxx     xxx    ',
    '      xx   xxx           xxxxxxxxx           xxx   xx      ',
    '      xx  xx                                   xx  xx      ',
    '       xxxx                                     xxxx       ']


shape1 = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']