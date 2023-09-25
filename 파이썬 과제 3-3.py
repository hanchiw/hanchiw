class Item:
    count = 0
    def __init__(self, t, p):
        self.t = t
        self.p = p
        Item.count += 1
    def __str__(self):
        return f'제목: {self.t}, 가격: {self.p}'
    def getprice(self):
        print(f'* {self.t} 의 가격은 {self.p} 원 입니다.')
class Book(Item):
    def __init__(self, t, p, pages, au):
        super().__init__(t, p)
        self.pages = pages
        self.au = au
    def __str__(self):
        return super().__str__() + f', 페이지 수: {self.pages}, 저자: {self.au}'
class Magazine(Item):
    def __init__(self, t, p, m):
        super().__init__(t, p)
        self.m = m
    def __str__(self):
        return super().__str__() + f', 출간 월: {self.m}'
if __name__ == '__main__':
    b1 = Book('소나기', 10000, 124, '황순원')
    b2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    b3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)
    print('', b1, '\n', b2, '\n', b3, '\n', magazine1, '\n', magazine2)
    print('총', Item.count, '권')
    b2.getprice()
    magazine1.getprice()
    b1.getprice()
