class Enemy:
    life = 3

    def attack(self):
        print('Ouch !')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('Dead')
        else:
            print(str(self.life) + ' '+ self.str)

    def __init__(self,s):
        print('Init Function')
        self.str=s

e1 = Enemy('Lives Left')
e1.attack()
e1.checkLife()
