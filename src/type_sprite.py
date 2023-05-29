from sprites import Board, Circle, Eks

def addCircle(c_x, c_y):
    circle = Circle()
    circle.rect.x = c_x
    circle.rect.y = c_y
    return circle
def addEks(c_x, c_y):
    eks = Eks()
    eks.rect.x = c_x
    eks.rect.y = c_y
    return eks